import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Configuration for running on SageMaker
if 'SM_MODEL_DIR' in os.environ:
    model_dir = os.environ['SM_MODEL_DIR']
    config = os.path.join(model_dir, 'config.json')
    tokenizer = os.path.join(model_dir, 'tokenizer')
    model = os.path.join(model_dir, 'pytorch_model.bin')
else:
    # Default configuration for local development
    config = 'bigscience/bloom/config.json'
    tokenizer = 'bigscience/bloom'
    model = 'bigscience/bloom/pytorch_model.bin'

bloom_pipeline = pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
    config=config
)

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    output = bloom_pipeline(prompt, max_length=100)
    return jsonify({'generated_text': output[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)