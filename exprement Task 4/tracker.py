import json
from datetime import datetime


# ---------- Run Model ----------
class Run:
    def __init__(self, run_id, params, metrics):
        self.run_id = run_id
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.params = params
        self.metrics = metrics

    def to_dict(self):
        return {
            "run_id": self.run_id,
            "timestamp": self.timestamp,
            "params": self.params,
            "metrics": self.metrics
        }


# ---------- Experiment Tracker ----------
class ExperimentTracker:

    def __init__(self, file_path="experiments.jsonl"):
        self.file_path = file_path

    # Save experiment
    def log_run(self, run_id, params, metrics):

        if not metrics:
            raise ValueError("Metrics required!")

        run = Run(run_id, params, metrics)

        with open(self.file_path, "a") as f:
            json.dump(run.to_dict(), f)
            f.write("\n")

        print(f"{run_id} saved successfully")

    # Load all runs
    def load_history(self):
        runs = []

        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    runs.append(json.loads(line))
        except FileNotFoundError:
            pass

        return runs

    # Find best run
    def best_run(self, metric_name):
        runs = self.load_history()

        if not runs:
            return None

        valid_runs = [
            r for r in runs
            if metric_name in r["metrics"]
        ]

        if metric_name.lower() == "loss":
            best = min(valid_runs,
                       key=lambda x: x["metrics"][metric_name])
        else:
            best = max(valid_runs,
                       key=lambda x: x["metrics"][metric_name])

        return best

    # Summary
    def summary(self):
        runs = self.load_history()

        print("\n----- SUMMARY -----")
        print("Total Runs:", len(runs))

        if not runs:
            return

        sorted_runs = sorted(
            runs,
            key=lambda x: x["metrics"].get("accuracy", 0),
            reverse=True
        )

        print("\nTop 3 Runs:")
        for r in sorted_runs[:3]:
            print(
                r["run_id"],
                "Accuracy:",
                r["metrics"].get("accuracy")
            )