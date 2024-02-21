# User Guide

## Getting Started

1. Clone the repository to your local machine using `git clone https://github.com/leyao-daily/KubeChat.git`.
2. Navigate to the project directory using `cd Kubechat/kserve`.

## Installation

Please first install the KServe
    
```bash
# Install kserve
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve.yaml

# Install kserve build-in cluster serving runtime (Optional)
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.11.0/kserve-runtimes.yaml
```


## Using the Files

This folder contains several files. Here's a brief description of what each file does:

- `llm.py`: This is the main file of the application. It contains the code for the main functionality of the application.
- `requirements.txt`: This file contains a list of Python packages that the application depends on. You can install these packages using `pip install -r requirements.txt`.
- `Dockerfile`: This file contains instructions for building a Docker image for the application.
- `deployment.yaml`: This file contains the configuration for the kserve deployment.
- `input.json`: This file contains the input data to test the llm inference
- `test.sh`: This file contains the command to test the llm inference

To use a file, you can typically open it in your text editor or run it in your terminal, depending on the file type.

## Running the Application

Before build the image, please check the Dockerfile and update the model path of your LLM model.

```bash
# Build the docker image
docker build -t <dockerhub_username>/llmserving:v0.1 .

# Push the docker image to dockerhub
docker push <dockerhub_username>/llmserving:v0.1

# Deploy the kserve
kubectl apply -f deployment.yaml

# Enable port forwarding
kubectl port-forward -n istio-system service/istio-ingressgateway 8080:80

# Test the inference
bash test.sh

```

## Running locally (conda)

```bash
# Download and install the conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Create a env (kserve support python < 3.12)
conda create -n llm python=3.11.7
conda activate llm

# Install dependencies
pip install torch==2.2.0+cpu torchvision==0.17.0+cpu torchaudio==2.2.0+cpu --index-url https://download.pytorch.org/whl/cpu 

pip install -r requirements.txt

# Run locally

python llm-local.py
