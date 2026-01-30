# Experiment 3: Containerizing ML Models with Docker

## Objective
Learn how to containerize a Machine Learning application using Docker for reproducible and portable deployments.

## Prerequisites
- Docker installed ([Download Docker](https://www.docker.com/products/docker-desktop))
- Basic understanding of ML and Python

## Project Structure
```
Exp3/
├── Dockerfile         # Docker configuration file
├── ML.py              # ML model training script (Iris classification)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## How to Run

### Step 1: Verify Docker Installation
```bash
docker --version
```

### Step 2: Build the Docker Image
Navigate to the Exp3 folder and run:
```bash
docker build -t ml-lab-model .
```
- `-t ml-lab-model` : Tags the image with the name "ml-lab-model"
- `.` : Uses the current directory's Dockerfile

### Step 3: Run the Docker Container
```bash
docker run ml-lab-model
```

### Expected Output
```
Model Accuracy: 1.0
```

## Files Description

| File | Description |
|------|-------------|
| `Dockerfile` | Defines the container environment (Python 3.10-slim base image) |
| `ML.py` | Trains a Logistic Regression model on the Iris dataset |
| `requirements.txt` | Lists dependencies: scikit-learn, numpy |

## Understanding the Dockerfile

```dockerfile
FROM python:3.10-slim      # Base image with Python 3.10
WORKDIR /app               # Set working directory inside container
COPY requirements.txt .    # Copy requirements file
RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies
COPY ML.py .               # Copy the ML script
CMD ["python", "ML.py"]    # Command to run when container starts
```

## Useful Docker Commands

| Command | Description |
|---------|-------------|
| `docker images` | List all Docker images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker rmi ml-iris-model` | Remove the image |
| `docker logs <container_id>` | View container logs |

## Running Without Docker (Optional)
```bash
pip install -r requirements.txt
python ML.py
```

## Key Concepts Learned
- Writing a Dockerfile for ML applications
- Building Docker images
- Running containers
- Containerization benefits: reproducibility, isolation, portability
