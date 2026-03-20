import logging
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
from prometheus_client import start_http_server, Gauge
import time

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="ml_system.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger()

# ---------------- PROMETHEUS METRICS ----------------
train_loss_gauge = Gauge('train_loss', 'Training Loss')
train_accuracy_gauge = Gauge('train_accuracy', 'Training Accuracy')

# Start Prometheus server
start_http_server(8000)

# ---------------- CUSTOM CALLBACK ----------------
class MonitoringCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}

        loss = logs.get('loss')
        acc = logs.get('accuracy')

        # Log to file
        logger.info(f"Epoch {epoch+1}: Loss={loss}, Accuracy={acc}")

        # Send metrics to Prometheus
        train_loss_gauge.set(loss)
        train_accuracy_gauge.set(acc)

# ---------------- DATASET ----------------
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

# ---------------- MODEL ----------------
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# ---------------- TENSORBOARD ----------------
tensorboard_callback = TensorBoard(log_dir="./logs")

# ---------------- TRAINING ----------------
model.fit(
    x_train, y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    callbacks=[MonitoringCallback(), tensorboard_callback]
)

print("Prometheus running at http://localhost:8000")

# Keep server alive
while True:
    time.sleep(1)