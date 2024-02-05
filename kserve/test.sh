#!/bin/bash

MODEL_NAME=llmserving
INPUT_PATH=input.json
SERVICE_HOSTNAME=$(kubectl get inferenceservice $MODEL_NAME -o jsonpath='{.status.url}' | cut -d "/" -f 3)

for i in {1..3}
do
   curl -v -H "Host: ${SERVICE_HOSTNAME}" http://localhost:8080/v1/models/${MODEL_NAME}:predict -d @./${INPUT_PATH} &
done
