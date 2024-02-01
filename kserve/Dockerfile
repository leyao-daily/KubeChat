FROM python:3.10-slim

WORKDIR /workspace

COPY requirements.txt ./

RUN pip install torch==2.0.1+cpu torchvision==0.15.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN pip install --no-cache-dir -r ./requirements.txt

COPY llama-2-7b-chat-hf ./llama-2-7b-chat-hf

COPY llm.py .

CMD ["python", "llm.py"]
