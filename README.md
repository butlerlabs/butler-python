# butler

      Welcome to Butler's Python SDK

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
*AppsApi* | [**get_app_run_status**](docs/AppsApi.md#get_app_run_status) | **GET** /api/apps/app_runs/{appRunId}/status | Get the status of an extraction job started by the upload_documents endpoint
*AppsApi* | [**get_document_extraction_results**](docs/AppsApi.md#get_document_extraction_results) | **GET** /api/apps/app_runs/{appRunId}/document_extraction | Get extracted results of an extraction job started by the upload_documents endpoint after it completes
*AppsApi* | [**upload_documents**](docs/AppsApi.md#upload_documents) | **POST** /api/apps/{appId}/upload_documents | Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /api/auth | Authenticates and authorizes the user to access the API
*QueuesApi* | [**get_extraction_results**](docs/QueuesApi.md#get_extraction_results) | **GET** /api/queues/{queueId}/extraction_results | Get paginated list of extraction results for documents matching the query params
*QueuesApi* | [**upload_documents_to_queue**](docs/QueuesApi.md#upload_documents_to_queue) | **POST** /api/queues/{queueId}/uploads | Upload documents to the queue specified by &lt;queueId&gt; for processing


## Documentation For Models

 - [AppRunStatus](docs/AppRunStatus.md)
 - [AppRunStatusDto](docs/AppRunStatusDto.md)
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
 - [LoginBodyDto](docs/LoginBodyDto.md)
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
