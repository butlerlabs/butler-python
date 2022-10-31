# Butler

Welcome to [Butler's Python SDK](https://butlerlabs.ai)

      Butler APIs are built on top of the OpenAPI 3.0 standard, and the SDK provides convenience
      functions to make programming easier

## Requirements.

Python >= 3.7

## Installation & Usage

### pip install

```sh
pip install butler-sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

from butler import Client

# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
api_key = '<api-key>'
# Get Queue ID from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#go-to-the-model-details-page
queue_id = '<queue_id>'
# Path to a local JPEG, PNG, or PDF file
local_file_path = 'example.pdf'

response = Client(api_key).extract_document(queue_id, local_file_path)
print(response)
```

If you are on version 0.0.5 of the SDK or older you will need a slight modification:
```python
response = Client(api_key).extract_document(local_file_path, queue_id)
```

## Maintain

```sh
PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```

To regenerate code to account for updates to REST API:

```sh
openapi-python-client update --url https://app.butlerlabs.ai/api/docs-json --config codegen.yaml
```

and make manual updates to `butler/__init.py__` if needed

To publish a new version:

Update `setup.py` to have a new version number

```sh
# build packages
python -m build

# upload to test pypi
python -m twine upload --repository testpypi --skip-existing dist/* --verbose

# test install from test pypi
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple butler-sdk

# Upload to real pypi if things checkout
python -m twine upload --skip-existing dist/* --verbose
```
