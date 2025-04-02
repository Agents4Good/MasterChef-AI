# Standard lib imports
import random
import pprint
from pathlib import Path
from time import perf_counter
# Third party imports
import numpy as np
from transformers import pipeline
from datasets import load_dataset
from evaluate import load
import torch

class PerformanceBenchmark:
    def __init__(self, pipeline, dataset, optim_type="BERT baseline"):
        self.pipeline = pipeline
        self.dataset = dataset
        self.optim_type = optim_type
    
    def compute_accuracy(self):
        accuracy_score = load("accuracy")
        intents = self.dataset.features["intent"]

        texts = [example["text"] for example in self.dataset]
        labels = [example["intent"] for example in self.dataset]

        predictions = self.pipeline(texts, batch_size=64)
        preds = [intents.str2int(pred["label"]) for pred in predictions]

        accuracy = accuracy_score.compute(predictions=preds, references=labels)
        print(f"Accuracy on test set = {accuracy['accuracy']:.3f}")
        return accuracy

    def compute_size(self):
        state_dict = self.pipeline.model.state_dict()
        tmp_path = Path("model.pt")
        torch.save(state_dict, tmp_path)
        size_mb = Path(tmp_path).stat().st_size / (1024 * 1024)
        tmp_path.unlink()
        print(f"Model size (MB) - {size_mb:.2f}")
        return {"size_mb": size_mb}

    def compute_latency(self):
        latencies = []

        for _ in range(10):
            # Get random sample
            sample = self.dataset[random.randint(0, len(self.dataset) - 1)]
            query = sample["text"]

            _ = self.pipeline(query)
        for _ in range(100):
            # Get random sample
            sample = self.dataset[random.randint(0, len(self.dataset) - 1)]
            query = sample["text"]

            start_time = perf_counter()
            _ = self.pipeline(query)
            latency = perf_counter() - start_time
            latencies.append(latency)

        time_avg_ms = 1000 * np.mean(latencies)
        time_std_ms = 1000 * np.std(latencies)
        print(f"Average latency (ms): {time_avg_ms:.2f} +- {time_std_ms:.2f}")
        return {"time_avg_ms": time_avg_ms, "time_std_ms": time_std_ms}

    def run_benchmark(self):
        metrics = {}
        metrics[self.optim_type] = {}
        metrics[self.optim_type].update(self.compute_size())
        metrics[self.optim_type].update(self.compute_accuracy())
        metrics[self.optim_type].update(self.compute_latency())
        return metrics


def main():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    bert_ckpt = "transformersbook/bert-base-uncased-finetuned-clinc"
    pipe = pipeline("text-classification",
                    model=bert_ckpt, device=0 if device == "cuda:0" else -1)

    clinc_ds = load_dataset("clinc_oos", "plus")
    benchmark = PerformanceBenchmark(pipe, clinc_ds["test"])
    pprint.pprint(benchmark.run_benchmark())


if __name__ == """__main__""":
    main()
