# Experiment 9: PyTorch to ONNX Conversion

## Objective
Train a simple PyTorch model, export it to ONNX format, and run inference using ONNX Runtime.

## Overview
This experiment demonstrates the basic ONNX workflow:
1. Define a simple neural network in PyTorch
2. Perform dummy training on random data
3. Export the trained model to `model.onnx`
4. Run inference with ONNX Runtime
5. Compare ONNX output with PyTorch output

## Files
- `onnx_experiment.py`: Main script for training, export, and inference
- `model.onnx`: Exported ONNX model generated after running the script

## Requirements
Install the following packages:
- `torch`
- `numpy`
- `onnxruntime`

## Installation
```bash
pip install torch numpy onnxruntime
```

## Running the Experiment
From the Exp9 folder, run:

```bash
python onnx_experiment.py
```

## What the Script Does
1. Creates a simple linear neural network with input size 4 and output size 3.
2. Trains the model for 100 epochs on randomly generated data.
3. Exports the trained model to ONNX using `torch.onnx.export()`.
4. Loads the exported model with ONNX Runtime.
5. Generates random input and runs inference.
6. Prints both ONNX and PyTorch outputs for comparison.

## Expected Output
When the script runs successfully, it prints messages similar to:

```text
Training Completed
Model Exported to ONNX

ONNX Output:
...

PyTorch Output:
...
```

## Notes
- The model is trained on random data only for demonstration purposes.
- `model.onnx` is overwritten each time the script is run.
- The ONNX export uses opset version `18` and a dynamic batch size axis.
- Small numerical differences between PyTorch and ONNX Runtime outputs are expected.
