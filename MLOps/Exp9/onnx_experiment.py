import torch
import torch.nn as nn
import numpy as np
import onnxruntime as ort

# -----------------------------------
# 1. Define Simple Neural Network
# -----------------------------------
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(4, 3)

    def forward(self, x):
        return self.fc(x)

# Create model
model = SimpleModel()

# -----------------------------------
# 2. Dummy Training
# -----------------------------------
x = torch.randn(20, 4)
y = torch.randn(20, 3)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

print("Training Completed")

# -----------------------------------
# 3. Export to ONNX
# -----------------------------------
dummy_input = torch.randn(1, 4)

torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={
        "input": {0: "batch_size"},
        "output": {0: "batch_size"}
    },
    opset_version=18
)

print("Model Exported to ONNX")

# -----------------------------------
# 4. ONNX Runtime Inference
# -----------------------------------
session = ort.InferenceSession("model.onnx")

input_data = np.random.randn(1, 4).astype(np.float32)

onnx_output = session.run(None, {"input": input_data})

print("\nONNX Output:")
print(onnx_output)

# -----------------------------------
# 5. Compare with PyTorch Output
# -----------------------------------
torch_output = model(torch.tensor(input_data))

print("\nPyTorch Output:")
print(torch_output.detach().numpy())