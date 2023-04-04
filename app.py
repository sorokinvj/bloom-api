import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

bloom_pipeline = pipeline(
    'text-generation',
    model='bigscience/bloom',
    tokenizer='bigscience/bloom'
)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    output = bloom_pipeline(prompt, max_length=100)
    return jsonify({'generated_text': output[0]['generated_text']})

if __name__ == '__main__':
    app.run()