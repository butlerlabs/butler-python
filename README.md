# Butler
Welcome to [Butler's Python SDK](https://butlerlabs.ai)

      Butler APIs are built on top of the OpenAPI 3.0 standard, and the SDK provides convenience
      functions to make programming easier

## Requirements.

Python >= 3.6

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

response = Client(api_key).extract_file('example.pdf', queue_id)
print(response)
```

## Documentation for API Endpoints
All URIs are relative to *https://app.butlerlabs.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*QueuesApi* | [**upload_documents_to_queue**](docs/QueuesApi.md#upload_documents_to_queue) | **POST** /api/queues/{queueId}/uploads | Upload documents to the queue specified by &lt;queueId&gt; for processing


## Documentation For Models

 - [DocExConfidence](docs/DocExConfidence.md)
 - [DocumentExtractionResultsDto](docs/DocumentExtractionResultsDto.md)
 - [DocumentStatus](docs/DocumentStatus.md)
 - [ExtraResultsDto](docs/ExtraResultsDto.md)
 - [ExtractedFieldDto](docs/ExtractedFieldDto.md)
 - [ExtractedTableCellDto](docs/ExtractedTableCellDto.md)
 - [ExtractedTableDto](docs/ExtractedTableDto.md)
 - [ExtractedTableRowDto](docs/ExtractedTableRowDto.md)
 - [ExtractionRangeDto](docs/ExtractionRangeDto.md)
 - [ExtractionResultsDto](docs/ExtractionResultsDto.md)
 - [ExtractionResultsSortBy](docs/ExtractionResultsSortBy.md)
 - [PaginatedExtractionResultsDto](docs/PaginatedExtractionResultsDto.md)
 - [SortOrder](docs/SortOrder.md)
 - [UploadDocumentResponseDto](docs/UploadDocumentResponseDto.md)
 - [UploadDocumentsUploadResponseDto](docs/UploadDocumentsUploadResponseDto.md)


## Documentation For Authorization


## bearer

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in butler.apis and butler.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from butler.api.default_api import DefaultApi`
- `from butler.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import butler
from butler.apis import *
from butler.models import *
```
## Maintain
```sh
pipenv install
```

To regenerate code to account for updates to REST API:
```sh
openapi-generator generate -i https://app.butlerlabs.ai/api/docs-json -g python --package-name butler
```
and make manual updates to `butler/__init.py` if needed

To publish a new version:

Update `setup.py` to have a new version number

```sh
# build packages
python -m build

# upload to test pypi
python -m twine upload --repository testpypi --skip-existing dist/* --verbose

# Upload to real pypi if things checkout
python -m twine upload --skip-existing dist/* --verbose
```
