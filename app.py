import os
from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

# Set OpenAI API key\

# API key from rohit@trustedweartech.com , being used as default
openai.api_key =""

# A key to pe passed with the requests to authenticate them
auth_key = 'Gn1TVEY49iCiLNBizXQyzJwqoMbSq1ra'


@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    auth = data['auth']
    question = data['question']
    model_engine = "text-davinci-003"
    if(auth == auth_key):

        # Call OpenAI ADA-001 API to get answer
        prompt = f"Q: {question}\nA:"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.0,
        )
        # Retrieve answer from OpenAI response
        answer = completions.choices[0].text.strip()

        return jsonify({'answer': answer})

    else:
        return ("Not authorized")


@app.route('/', methods=['GET'])
def get_hello():
    return ("Welcome to the ChatGPT API! \n ©Private Property of Trustedwear Tech. \n Contact rohit@trustedweartech.com for any queries...")


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    from waitress import serve
    serve(app, host="0.0.0.0", port=server_port)
