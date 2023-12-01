import requests

# URLs for the services
EMBEDDING_SERVICE_URL = "http://localhost:5001"
LLM_SERVICE_URL = "http://localhost:5002"
PROMPT_SERVICE_URL = "http://localhost:5000"

def generate_embeddings(file_path):
    try:
        response = requests.post(f"{EMBEDDING_SERVICE_URL}/generate_embeddings", json={"file_path": file_path})
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print("Error in generating embeddings:", e)
        return False

def search_embeddings(query):
    try:
        response = requests.post(f"{EMBEDDING_SERVICE_URL}/search", json={"query": query})
        response.raise_for_status()
        return response.json()["results"]
    except requests.RequestException as e:
        print("Error in search:", e)
        return None

def get_prompt(template_id):
    try:
        response = requests.post(f"{PROMPT_SERVICE_URL}/get_prompt", json={"template_id": template_id})
        response.raise_for_status()
        return response.json()["prompt"]
    except requests.RequestException as e:
        print("Error in getting prompt:", e)
        return None

def process_llm(prompt, context, question):
    try:
        response = requests.post(f"{LLM_SERVICE_URL}/process", json={"prompt": prompt, "context": context, "question": question})
        response.raise_for_status()
        return response.json()["response"]
    except requests.RequestException as e:
        print("Error in LLM processing:", e)
        return None

def main():
    default_file_path = "example.txt"
    default_template_id = "template1"
    
    file_path = input(f"Enter the file path (default: {default_file_path}): ")
    file_path = file_path if file_path else default_file_path

    template_id = input(f"Enter the template ID (default: {default_template_id}): ")
    template_id = template_id if template_id else default_template_id

    if not generate_embeddings(file_path):
        print("Failed to generate embeddings.")
        return

    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        prompt_template = get_prompt(template_id)
        if prompt_template:
            print("Prompt Template:", prompt_template)
        else:
            print("Prompt template not found.")
            continue

        answer = process_llm(prompt_template, "", question)
        if answer:
            print("LLM Service Answer:", answer)
        else:
            print("No answer generated.")

if __name__ == "__main__":
    main()
