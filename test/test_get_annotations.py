import os

from butler import Client

# Run using 'python -m test.test_get_annotations'

# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
api_key = os.environ['BUTLER_API_KEY']

# Find your model's id
model_id = '7b4f6c88-071a-4ecc-8b96-c38a9eaaa93a'

response = Client(api_key).load_annotations(
  model_id,
  load_all_documents=True,
)

print(response)