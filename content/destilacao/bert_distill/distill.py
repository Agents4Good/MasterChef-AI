import numpy as np
import torch
from transformers import AutoTokenizer, AutoConfig
from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from datasets import load_dataset
from evaluate import load
from trainer import TrainingArgumentsDistill, TrainerDistill


device = "cuda:0" if torch.cuda.is_available() else "cpu"


def tokenize_dataset(dataset, tokenizer):
    # Create input_ids column with tokens and remove text column
    clinc_enc = dataset.map(
        lambda batch: tokenizer(batch["text"], truncation=True),
        batched=True,
        remove_columns=["text"]
    )
    clinc_enc = clinc_enc.rename_column("intent", "labels")
    return clinc_enc


def compute_metrics(pred):
    accuracy_score = load("accuracy")
    logits, labels = pred
    predictions = np.argmax(logits, axis=1)
    return accuracy_score.compute(predictions=predictions, references=labels)


def student_init(model, config):
    return (AutoModelForSequenceClassification.from_pretrained(
            model, config=config).to(device))


def distill():
    teacher_ckpt = "transformersbook/bert-base-uncased-finetuned-clinc"
    # teacher_ckpt = "textattack/bert-base-uncased-imdb"
    student_ckpt = "distilbert-base-uncased"
    pipe = pipeline("text-classification", model=teacher_ckpt,
                    device=0 if device == "cuda:0" else -1)
    tokenizer = AutoTokenizer.from_pretrained(student_ckpt)

    # Prepare dataset
    clinc_ds = load_dataset("clinc_oos", "plus")
    clinc_enc = tokenize_dataset(clinc_ds, tokenizer)

    # Create custom configuration with label mappings
    id2label = pipe.model.config.id2label
    label2id = pipe.model.config.label2id
    intents = clinc_ds["test"].features["intent"]
    num_labels = intents.num_classes

    student_config = (AutoConfig.from_pretrained(
        student_ckpt, num_labels=num_labels,
        id2label=id2label, label2id=label2id
    ))


    batch_size = 48
    output_dir = "distilbert-base-uncased-finetuned-clinc"
    student_training_args = TrainingArgumentsDistill(
        output_dir=output_dir, evaluation_strategy="epoch",
        num_train_epochs=5, learning_rate=2e-5,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        alpha=1, weight_decay=0.01
    )


    # Training
    teacher_model = (AutoModelForSequenceClassification.from_pretrained(
                     teacher_ckpt, num_labels=num_labels).to(device))

    distilbert_trainer = TrainerDistill(
        model_init=(lambda x: student_init(student_ckpt, student_config)),
        teacher_model=teacher_model, args=student_training_args,
        train_dataset=clinc_enc["train"], eval_dataset=clinc_enc["validation"],
        compute_metrics=compute_metrics, tokenizer=tokenizer
    )

    distilbert_trainer.train()


if __name__ == """__main__""":
    distill()
