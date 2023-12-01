import requests

# URLs for the services
EMBEDDING_SERVICE_URL = "http://localhost:5001"
LLM_SERVICE_URL = "http://localhost:5002"
PROMPT_SERVICE_URL = "http://localhost:5000"

def generate_embeddings(file_path):
    """Send a request to the Embedding Service to generate embeddings."""
    response = requests.post(f"{EMBEDDING_SERVICE_URL}/generate_embeddings", json={"file_path": file_path})
    if response.status_code == 200:
        return True
    else:
        print("Error in generating embeddings:", response.json())
        return False

def search_embeddings(query):
    """Send a search query to the Embedding Service."""
    response = requests.post(f"{EMBEDDING_SERVICE_URL}/search", json={"query": query})
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Error in search:", response.json())
        return None

def get_prompt(template_id):
    """Retrieve a prompt from the Prompt Service."""
    response = requests.post(f"{PROMPT_SERVICE_URL}/get_prompt", json={"template_id": template_id})
    if response.status_code == 200:
        return response.json()["prompt"]
    else:
        print("Error in getting prompt:", response.json())
        return None

def process_llm(prompt, context, question):
    """Send a request to the LLM Service to process the prompt."""
    response = requests.post(f"{LLM_SERVICE_URL}/process", json={"prompt": prompt, "context": context, "question": question})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print("Error in LLM processing:", response.json())
        return None

# Example Usage
file_path = "./example.txt"
question = "What does Cloud Native mean?"
#question = "What is AI?"
template_id = "template1"

# Generate embeddings
if generate_embeddings(file_path):
    # Search embeddings
    context = search_embeddings(question)
    if context:
        print("Search Results:", "Success")
    
    # Get prompt
    prompt_template = get_prompt(template_id)
    if prompt_template:        
        # Process with LLM
        answer = process_llm(prompt_template, context, question)
        if answer:
            print("LLM Service Answer:", answer)
