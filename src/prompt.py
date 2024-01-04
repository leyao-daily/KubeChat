from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for prompt templates
prompt_templates = {
    "template1": {
        "template": """This is a AI Chatbot, which can chat with you about what it knows.

Input: {input}
Answer:""",
        "version": 1
    },
    "template2": {
        "template": """Use the following pieces of context to answer the question at the end.
{context}
question: {question}
answer:""",
        "version": 1
    },
    # Additional templates...
}

@app.route('/get_prompt', methods=['POST'])
def get_prompt():
    data = request.json
    template_id = data.get('template_id')

    if template_id not in prompt_templates:
        return jsonify({"error": "Template not found"}), 404

    prompt_data = prompt_templates[template_id]

    # Render the prompt with the provided variables
    return jsonify({"prompt": prompt_data["template"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
