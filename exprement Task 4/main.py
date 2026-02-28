from tracker import ExperimentTracker


tracker = ExperimentTracker()

# Add experiments
tracker.log_run(
    "run_1",
    {"learning_rate": 0.01, "epochs": 10},
    {"accuracy": 0.82, "loss": 0.4}
)

tracker.log_run(
    "run_2",
    {"learning_rate": 0.001, "epochs": 20},
    {"accuracy": 0.90, "loss": 0.2}
)

tracker.log_run(
    "run_3",
    {"learning_rate": 0.1, "epochs": 5},
    {"accuracy": 0.75, "loss": 0.5}
)

# Best run
best = tracker.best_run("accuracy")

print("\nBest Run:")
print(best)

# Summary
tracker.summary()