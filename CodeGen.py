import boto3
import json 

def generate_code(prompt_data):
    bedrock = boto3.client(service_name="bedrock-runtime")

    payload = {
        "prompt": "Human: " + prompt_data + "\nAssistant:",  
        "max_tokens_to_sample": 2048,  
        "top_k": 250,
        "top_p": 1
    }
    body = json.dumps(payload)
    model_id = "anthropic.claude-v2"

    response = bedrock.invoke_model(
        body=body, 
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response.get("body").read())
    response_text = response_body['conompleti']  
    return response_text

# # Example usage
# prompt_data = "Write a Python function that calculates the factorial of a number."
# print(generate_code(prompt_data))
