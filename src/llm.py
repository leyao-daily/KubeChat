from flask import Flask, request, jsonify
from langchain.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

app = Flask(__name__)
llm = LlamaCpp(
    model_path="./model/llama-2-7b-chat.Q8_0.gguf",
    temperature=0.75,
    top_p=1,
    )

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    prompt = PromptTemplate(template=data['prompt'], input_variables=["context", "question"])
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.run({"context": data["context"], "question": data['question']})
    print(response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
