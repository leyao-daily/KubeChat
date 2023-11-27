from flask import Flask, request, jsonify
from langchain.embeddings import LlamaCppEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

app = Flask(__name__)
embeddings_model = LlamaCppEmbeddings(model_path="./model/llama-2-7b-chat.Q8_0.gguf")
chroma_db = Chroma

@app.route('/generate_embeddings', methods=['POST'])
def generate_embeddings():
    global chroma_db
    file_path = request.json.get('file_path', '')

    if not file_path:
        return jsonify({"error": "No file path provided"}), 400

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        loader = TextLoader(file_path)
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
        text = splitter.split_documents(docs)
        chroma_db = Chroma.from_documents(text, embeddings_model) 

        return jsonify({"Success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['POST'])
def search():
    global chroma_db
    query = request.json.get('query', '')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Search in the vector database
        results = chroma_db.similarity_search(query, k=1)
        results = results[0].page_content
    
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
