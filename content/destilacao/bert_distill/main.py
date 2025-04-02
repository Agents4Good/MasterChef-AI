import pprint
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.quantization import quantize_dynamic
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset
from benchmark import PerformanceBenchmark

device = "cuda:0" if torch.cuda.is_available() else "cpu"


def plot_metrics(perf_metrics, current_optim_type):
    df = pd.DataFrame.from_dict(perf_metrics, orient="index")

    for idx in df.index:
        df_opt = df.loc[idx]
        if idx == current_optim_type:
            plt.scatter(df_opt["time_avg_ms"], df_opt["accuracy"] * 100,
                        alpha=0.5, s=df_opt["size_mb"], label=idx,
                        marker="$\u25CC$")
        else:
            plt.scatter(df_opt["time_avg_ms"], df_opt["accuracy"] * 100,
                        s=df_opt["size_mb"], label=idx, alpha=0.5)

    legend = plt.legend(bbox_to_anchor=(1, 1))
    for handle in legend.legend_handles:
        handle.set_sizes([20])

    plt.ylim(80, 90)
    xlim = int(perf_metrics["BERT baseline"]["time_avg_ms"] + 3)
    plt.xlim(1, xlim)
    plt.ylabel("Accuracy (%)")
    plt.xlabel("Average latency (ms)")
    plt.show()


def quantize_model(model):
    # Apply dynamic quantization to the model (only quantizing nn.Linear layers)
    quantized_model = quantize_dynamic(model, {nn.Linear}, dtype=torch.qint8)
    return quantized_model


def main():
    clinc_ds = load_dataset("clinc_oos", "plus")
    perf_metrics = {}

    # Fine-tuned BERT
    bert_ckpt = "transformersbook/bert-base-uncased-finetuned-clinc"
    bert_pipe = pipeline("text-classification",
                         model=bert_ckpt, device=0 if device == "cuda:0" else -1)
    pb = PerformanceBenchmark(bert_pipe, clinc_ds["test"])
    perf_metrics.update(pb.run_benchmark())
    bert_pipe.model.to("cpu")     # Free space from VRAM

    # Distilled BERT
    distilbert_ckpt = "./distilbert-base-uncased-finetuned-clinc/checkpoint-1590"
    model = AutoModelForSequenceClassification.from_pretrained(distilbert_ckpt)
    tokenizer = AutoTokenizer.from_pretrained(distilbert_ckpt)
    distilbert_pipe = pipeline("text-classification", model=model,
                               tokenizer=tokenizer,
                               device=0 if device == "cuda:0" else -1)
    pb = PerformanceBenchmark(distilbert_pipe, clinc_ds["test"], optim_type="DistilBERT")
    perf_metrics.update(pb.run_benchmark())
    distilbert_pipe.model.to("cpu")

    # Quantized DistilBERT
    q8_distilbert = quantize_model(model)  # Pass the model directly, not the pipeline
    q8_distilbert_pipe = pipeline("text-classification", model=q8_distilbert,
                                  tokenizer=tokenizer, device=-1)

    # Benchmark the quantized model
    pb = PerformanceBenchmark(q8_distilbert_pipe, clinc_ds["test"], optim_type="Quant-DistilBERT")
    perf_metrics.update(pb.run_benchmark())
    q8_distilbert.to("cpu")  # Move quantized model to CPU to free up GPU memory if using CUDA


    pprint.pprint(perf_metrics)
    plot_metrics(perf_metrics, current_optim_type="DistilBERT")


if __name__ == """__main__""":
    main()
