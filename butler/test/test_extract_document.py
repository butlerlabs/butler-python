import logging
import os

from butler import Client
from butler.annotations.layoutlm_utils import normalize_ner_annotation_for_layoutlm

# Run using 'python -m butler.test.test_extract_document'

logging.basicConfig(level=logging.INFO)

# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
api_key = os.environ["BUTLER_API_KEY"]

# Find your queue's uuid
queue_id = "00000000-0000-0000-0000-000000000000"

# Get a local test file
local_file = "path/to/file"

extraction_results = Client(api_key).extract_document(queue_id, local_file)

print(extraction_results)
