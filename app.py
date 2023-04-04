from transformers import pipeline
import json

bloom_pipeline = pipeline(
    'text-generation',
    model='bigscience/bloom',
    tokenizer='bigscience/bloom'
)

def lambda_handler(event, context):
    if 'body' in event:
        body = json.loads(event['body'])
        prompt = body['prompt']
        output = bloom_pipeline(prompt, max_length=100)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"generated_text": output[0]['generated_text']})
        }
    else:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"message": "Request body not found"})
        }