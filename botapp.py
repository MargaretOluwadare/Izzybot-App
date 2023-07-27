from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__, template_folder="templates")
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_query = request.json.get('user_query', '')  # Using request.json to access JSON data
        if user_query:
            response = generate_response(user_query)
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'No user_query found in the request.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_response(query):
    return generator(query, max_length=100)[0]['generated_text']

if __name__ == '__main__':
    app.debug=True
    app.run()
