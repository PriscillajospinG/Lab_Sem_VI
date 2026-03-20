# Experiment 8: ML System Monitoring (TensorBoard + Prometheus)

## Objective
Build a simple ML training pipeline and monitor it using:
- Python logging (training events)
- TensorBoard (training and validation curves)
- Prometheus metrics (live loss and accuracy)

## Files
- `ml.py`: Main training and monitoring script
- `logs/`: TensorBoard event logs (generated during training)
- `ml_system.log`: File logs with epoch-wise metrics
- `ml_env/`: Local Python virtual environment (optional)

## What the Script Does
1. Loads the MNIST dataset from TensorFlow.
2. Builds and trains a neural network model for 5 epochs.
3. Logs epoch-wise `loss` and `accuracy` to `ml_system.log`.
4. Exposes live metrics via Prometheus on port `8000`.
5. Writes training and validation events for TensorBoard in `./logs`.
6. Keeps the process alive after training so Prometheus metrics stay available.

## Prerequisites
- Python 3.10+
- pip

## Installation
Install dependencies:

```bash
pip install tensorflow==2.15
pip install protobuf==3.20.3
pip install prometheus_client
pip install tensorboard
```

## Run the Experiment
From this folder:

```bash
python ml.py
```

After training completes, the script prints:

```text
Prometheus running at http://localhost:8000
```

The process continues running by design. Use `Ctrl + C` to stop it.

## Monitoring
### 1) Prometheus Metrics Endpoint
Open:

- `http://localhost:8000/metrics`

Custom metrics exposed:
- `train_loss`
- `train_accuracy`

### 2) TensorBoard
Run in another terminal:

```bash
tensorboard --logdir=logs
```

Then open:

- `http://localhost:6006`

## Log File
Training logs are written to:

- `ml_system.log`

Each epoch logs values in this format:

```text
YYYY-MM-DD HH:MM:SS,mmm INFO Epoch X: Loss=..., Accuracy=...
```

## Notes
- Port `8000` must be free for Prometheus metrics server.
- If you rerun the script, existing logs may accumulate.
- This experiment is focused on observability, not model optimization.
