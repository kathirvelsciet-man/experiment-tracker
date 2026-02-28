# experiment-tracker
Python-based experiment tracking system that logs experiment parameters and metrics, stores run history in JSONL format, and identifies the best experiment run based on performance metrics.
## Task 4: Experiment Tracker (File-Based Run History)

### Objective

To develop a file-based experiment tracking system that records experiment runs, stores parameters and metrics, reloads experiment history, and identifies the best-performing run.

### Description

In this task, an Experiment Tracker application was implemented using Python to manage experiment executions efficiently. Each experiment run is logged with its parameters and performance metrics and stored in JSONL format. The tracker allows users to reload previous experiment history and analyze results to determine the best experiment based on selected evaluation metrics such as accuracy or loss.

### Tasks Performed

* Defined experiment run model with unique run ID
* Recorded experiment timestamp automatically
* Stored experiment parameters and metrics
* Implemented ExperimentTracker class
* Logged experiment runs into JSONL file
* Loaded experiment history from stored records
* Validated required performance metrics
* Identified best run based on given metric
* Generated experiment summary statistics
* Displayed total runs and top-performing experiments

### Tools Used

* Python
* JSON Handling
* JSONL File Storage
* Logging Module
* VS Code

### Run Fields

Each experiment run contains:

* **run_id** – Unique experiment identifier
* **timestamp** – Execution time of experiment
* **params** – Dictionary of experiment parameters
* **metrics** – Dictionary of evaluation metrics

### Output Files

* **runs.jsonl** – Stored experiment run history
* **log.txt** – Execution logs and tracking details

### Result

The Experiment Tracker successfully logs experiment runs, maintains historical records, reloads experiment data, and identifies the best-performing experiment based on selected evaluation metrics such as highest accuracy or lowest loss.

