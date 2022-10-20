# butler.AppsApi

All URIs are relative to *https://app.butlerlabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_run_status**](AppsApi.md#get_app_run_status) | **GET** /api/apps/app_runs/{appRunId}/status | Get the status of an extraction job started by the upload_documents endpoint
[**get_document_extraction_results**](AppsApi.md#get_document_extraction_results) | **GET** /api/apps/app_runs/{appRunId}/document_extraction | Get extracted results of an extraction job started by the upload_documents endpoint after it completes
[**upload_documents**](AppsApi.md#upload_documents) | **POST** /api/apps/{appId}/upload_documents | Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results


# **get_app_run_status**
> AppRunStatusDto get_app_run_status(app_run_id)

Get the status of an extraction job started by the upload_documents endpoint

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import apps_api
from butler.model.app_run_status_dto import AppRunStatusDto
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
    api_instance = apps_api.AppsApi(api_client)
    app_run_id = "appRunId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the status of an extraction job started by the upload_documents endpoint
        api_response = api_instance.get_app_run_status(app_run_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling AppsApi->get_app_run_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_run_id** | **str**|  |

### Return type

[**AppRunStatusDto**](AppRunStatusDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get App Run status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_extraction_results**
> [DocumentExtractionResultsDto] get_document_extraction_results(app_run_id)

Get extracted results of an extraction job started by the upload_documents endpoint after it completes

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import apps_api
from butler.model.document_extraction_results_dto import DocumentExtractionResultsDto
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
    api_instance = apps_api.AppsApi(api_client)
    app_run_id = "appRunId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get extracted results of an extraction job started by the upload_documents endpoint after it completes
        api_response = api_instance.get_document_extraction_results(app_run_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling AppsApi->get_document_extraction_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_run_id** | **str**|  |

### Return type

[**[DocumentExtractionResultsDto]**](DocumentExtractionResultsDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get extracted results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents**
> upload_documents(app_id)

Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import apps_api
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
    api_instance = apps_api.AppsApi(api_client)
    app_id = "appId_example" # str | 
    extra_results = [
        "LineBlocks",
    ] # [str] | Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default (optional)
    files = open('/path/to/file', 'rb') # [file_type] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results
        api_instance.upload_documents(app_id)
    except butler.ApiException as e:
        print("Exception when calling AppsApi->upload_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results
        api_instance.upload_documents(app_id, extra_results=extra_results, files=files)
    except butler.ApiException as e:
        print("Exception when calling AppsApi->upload_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  |
 **extra_results** | **[str]**| Which extra results to generate, if any. These are lower-level results that you may use in your own post-processing. Omitted by default | [optional]
 **files** | **[file_type]**|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

