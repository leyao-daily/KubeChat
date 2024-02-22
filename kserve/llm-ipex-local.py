import torch
import intel_extension_for_pytorch as ipex
import json
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
from kserve import Model, ModelServer
import ray
from ray import serve
ray.init(dashboard_host="0.0.0.0")

@serve.deployment(
    name="llmserving", 
    max_concurrent_queries=100,
    graceful_shutdown_wait_loop_s=22,
    graceful_shutdown_timeout_s=2000,
    health_check_period_s=102,
    health_check_timeout_s=302,
    ray_actor_options={
        "num_cpus": 10,
        "runtime_env": {
            "MKL_NUM_THREADS": 10,
            "OMP_NUM_THREADS": 10,
            "TF_WARNING": None,
            "USE_MLLDNN": '1',
            "USE_OPENMP": '1',
            },
        },
    num_replicas=1,
)
class LLaMAModel(Model):
    def __init__(self):
        self.name = "llama-model"
        super().__init__(self.name)
        self.model_dir = "./llama-2-7b-chat-hf"
        self.model = None
        self.tokenizer = None
        self.load()

    def load(self):
        # Load the tokenizer and model here
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_dir)
        #self.model.eval()
        self.model = self.model.to(memory_format=torch.channels_last)
        self.model = ipex.optimize(self.model.eval(), dtype=torch.bfloat16)

    def predict(self, request, headers):
        # Check if request needs to be decoded from bytes
        data = json.loads(request.decode('utf-8'))

        input_text = data["instances"][0]["text"]
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')

        start_time = time.time()

        with torch.no_grad(), torch.inference_mode(), torch.cpu.amp.autocast():
            output = self.model.generate(input_ids, max_length=100)

        end_time = time.time()
        inference_time = end_time - start_time
        num_generated_tokens = len(self.tokenizer.decode(output[0], skip_special_tokens=False).split())
        tokens_per_second = num_generated_tokens / inference_time

        response_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return {"predictions": [response_text], "tokens_per_second": tokens_per_second}

if __name__ == "__main__":
    ModelServer().start({"llmserving": LLaMAModel})
