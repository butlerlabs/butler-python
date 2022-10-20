# butler.QueuesApi

All URIs are relative to *https://app.butlerlabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_document**](QueuesApi.md#extract_document) | **POST** /api/queues/{queueId}/documents | Upload a single document to the queue specified by &lt;queueId&gt; and returns the extracted results
[**get_extraction_results**](QueuesApi.md#get_extraction_results) | **GET** /api/queues/{queueId}/extraction_results | Get paginated list of extraction results for documents matching the query params
[**upload_documents_to_queue**](QueuesApi.md#upload_documents_to_queue) | **POST** /api/queues/{queueId}/uploads | Upload documents to the queue specified by &lt;queueId&gt; for processing


# **extract_document**
> ExtractionResultsDto extract_document(queue_id)

Upload a single document to the queue specified by <queueId> and returns the extracted results

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import queues_api
from butler.model.extraction_results_dto import ExtractionResultsDto
from pprint import pprint
# Defining the host is optional and defaults to https://app.butlerlabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = butler.Configuration(
    host = "https://app.butlerlabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = butler.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with butler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    queue_id = "queueId_example" # str | ID of the queue
    extra_results = [
        "LineBlocks",
    ] # [str] | Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default (optional)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a single document to the queue specified by <queueId> and returns the extracted results
        api_response = api_instance.extract_document(queue_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->extract_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a single document to the queue specified by <queueId> and returns the extracted results
        api_response = api_instance.extract_document(queue_id, extra_results=extra_results, file=file)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->extract_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| ID of the queue |
 **extra_results** | **[str]**| Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default | [optional]
 **file** | **file_type**|  | [optional]

### Return type

[**ExtractionResultsDto**](ExtractionResultsDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns extracted results for the document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extraction_results**
> PaginatedExtractionResultsDto get_extraction_results(queue_id, upload_id)

Get paginated list of extraction results for documents matching the query params

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import queues_api
from butler.model.paginated_extraction_results_dto import PaginatedExtractionResultsDto
from butler.model.extraction_results_sort_by import ExtractionResultsSortBy
from butler.model.sort_order import SortOrder
from pprint import pprint
# Defining the host is optional and defaults to https://app.butlerlabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = butler.Configuration(
    host = "https://app.butlerlabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = butler.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with butler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    queue_id = "queueId_example" # str | ID of the queue
    upload_id = "uploadId_example" # str | ID of an upload
    after_id = "afterId_example" # str | Fetch a page of results after this ID (optional)
    before_id = "beforeId_example" # str | Fetch a page of results before this ID (optional)
    limit = 3.14 # float | Number of results per page (optional)
    sort_order = SortOrder("Asc") # SortOrder | Sort order. Default is ascending order. (optional)
    extra_results = [
        "LineBlocks",
    ] # [str] | Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default (optional)
    sort_by = ExtractionResultsSortBy("DocumentId") # ExtractionResultsSortBy | Attribute to sort by. Default is DocumentId (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get paginated list of extraction results for documents matching the query params
        api_response = api_instance.get_extraction_results(queue_id, upload_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->get_extraction_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get paginated list of extraction results for documents matching the query params
        api_response = api_instance.get_extraction_results(queue_id, upload_id, after_id=after_id, before_id=before_id, limit=limit, sort_order=sort_order, extra_results=extra_results, sort_by=sort_by)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->get_extraction_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| ID of the queue |
 **upload_id** | **str**| ID of an upload |
 **after_id** | **str**| Fetch a page of results after this ID | [optional]
 **before_id** | **str**| Fetch a page of results before this ID | [optional]
 **limit** | **float**| Number of results per page | [optional]
 **sort_order** | **SortOrder**| Sort order. Default is ascending order. | [optional]
 **extra_results** | **[str]**| Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default | [optional]
 **sort_by** | **ExtractionResultsSortBy**| Attribute to sort by. Default is DocumentId | [optional]

### Return type

[**PaginatedExtractionResultsDto**](PaginatedExtractionResultsDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a page of extraction results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents_to_queue**
> UploadDocumentsUploadResponseDto upload_documents_to_queue(queue_id)

Upload documents to the queue specified by <queueId> for processing

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import queues_api
from butler.model.upload_documents_upload_response_dto import UploadDocumentsUploadResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://app.butlerlabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = butler.Configuration(
    host = "https://app.butlerlabs.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = butler.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with butler.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = queues_api.QueuesApi(api_client)
    queue_id = "queueId_example" # str | ID of the queue
    extra_results = [
        "LineBlocks",
    ] # [str] | Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default (optional)
    files = open('/path/to/file', 'rb') # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload documents to the queue specified by <queueId> for processing
        api_response = api_instance.upload_documents_to_queue(queue_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->upload_documents_to_queue: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload documents to the queue specified by <queueId> for processing
        api_response = api_instance.upload_documents_to_queue(queue_id, extra_results=extra_results, files=files)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling QueuesApi->upload_documents_to_queue: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| ID of the queue |
 **extra_results** | **[str]**| Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default | [optional]
 **files** | **[file_type]**|  | [optional]

### Return type

[**UploadDocumentsUploadResponseDto**](UploadDocumentsUploadResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the upload id for the initiated upload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

