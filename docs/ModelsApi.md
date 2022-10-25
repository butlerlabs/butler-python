# butler.ModelsApi

All URIs are relative to *https://app.butlerlabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_model**](ModelsApi.md#create_custom_model) | **POST** /api/models | 
[**get_document_enhanced_results**](ModelsApi.md#get_document_enhanced_results) | **GET** /api/models/{id}/documents/{documentId}/enhanced_results | 
[**get_model**](ModelsApi.md#get_model) | **GET** /api/models/{id} | 
[**get_training_document**](ModelsApi.md#get_training_document) | **GET** /api/models/{id}/training_documents/{documentId} | 
[**get_training_documents**](ModelsApi.md#get_training_documents) | **GET** /api/models/{id}/training_documents | 
[**train_custom_model**](ModelsApi.md#train_custom_model) | **POST** /api/models/{id}/train | Train a model
[**update_document_labels**](ModelsApi.md#update_document_labels) | **PUT** /api/models/{id}/documents/{documentId}/labels | Update labels for a specific document


# **create_custom_model**
> ModelInfoDto create_custom_model(create_model_dto)



Create a new custom model

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.create_model_dto import CreateModelDto
from butler.model.model_info_dto import ModelInfoDto
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
    api_instance = models_api.ModelsApi(api_client)
    create_model_dto = CreateModelDto(
        name="name_example",
        fields=[
            FieldDto(
                name="name_example",
                type=ModelFieldType("Text"),
            ),
        ],
        tables=[
            TableDto(
                name="name_example",
                columns=[
                    ColumnDto(
                        name="name_example",
                    ),
                ],
            ),
        ],
    ) # CreateModelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_custom_model(create_model_dto)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->create_custom_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_model_dto** | [**CreateModelDto**](CreateModelDto.md)|  |

### Return type

[**ModelInfoDto**](ModelInfoDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details of the created model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_enhanced_results**
> DocumentEnhancedResultDto get_document_enhanced_results(id, document_id)



Get enhanced results for a document

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.document_enhanced_result_dto import DocumentEnhancedResultDto
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.
    document_id = "documentId_example" # str | The id of the document.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_document_enhanced_results(id, document_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->get_document_enhanced_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |
 **document_id** | **str**| The id of the document. |

### Return type

[**DocumentEnhancedResultDto**](DocumentEnhancedResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns enhanced results for a document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> ModelInfoDto get_model(id)



Get details of a model

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.model_info_dto import ModelInfoDto
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_model(id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |

### Return type

[**ModelInfoDto**](ModelInfoDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details of a model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_document**
> TrainingDocumentResultDto get_training_document(id, document_id)



Get the details of a specific training document

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.training_document_result_dto import TrainingDocumentResultDto
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.
    document_id = "documentId_example" # str | The id of the document.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_training_document(id, document_id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->get_training_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |
 **document_id** | **str**| The id of the document. |

### Return type

[**TrainingDocumentResultDto**](TrainingDocumentResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the details of a specific training document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_documents**
> PaginatedTrainingDocumentsDto get_training_documents(id)



Get training documents for the specified model

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.sort_order import SortOrder
from butler.model.model_training_document_status import ModelTrainingDocumentStatus
from butler.model.paginated_training_documents_dto import PaginatedTrainingDocumentsDto
from butler.model.training_details_sort_by import TrainingDetailsSortBy
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.
    after_id = "afterId_example" # str | Fetch a page of results after this ID (optional)
    before_id = "beforeId_example" # str | Fetch a page of results before this ID (optional)
    limit = 3.14 # float | Number of results per page (optional)
    sort_order = SortOrder("Asc") # SortOrder | Sort order. Default is ascending order. (optional)
    sort_by = TrainingDetailsSortBy("CreatedAt") # TrainingDetailsSortBy | Attribute to sort by. Default is CreatedAt (optional)
    document_status = ModelTrainingDocumentStatus("OcrInProgress") # ModelTrainingDocumentStatus | Training document status to filter by (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_training_documents(id)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->get_training_documents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_training_documents(id, after_id=after_id, before_id=before_id, limit=limit, sort_order=sort_order, sort_by=sort_by, document_status=document_status)
        pprint(api_response)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->get_training_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |
 **after_id** | **str**| Fetch a page of results after this ID | [optional]
 **before_id** | **str**| Fetch a page of results before this ID | [optional]
 **limit** | **float**| Number of results per page | [optional]
 **sort_order** | **SortOrder**| Sort order. Default is ascending order. | [optional]
 **sort_by** | **TrainingDetailsSortBy**| Attribute to sort by. Default is CreatedAt | [optional]
 **document_status** | **ModelTrainingDocumentStatus**| Training document status to filter by | [optional]

### Return type

[**PaginatedTrainingDocumentsDto**](PaginatedTrainingDocumentsDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of training documents for the specified model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **train_custom_model**
> train_custom_model(id)

Train a model

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.

    # example passing only required values which don't have defaults set
    try:
        # Train a model
        api_instance.train_custom_model(id)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->train_custom_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns successful if training is started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_labels**
> update_document_labels(id, document_id, put_document_labels_dto)

Update labels for a specific document

### Example

* Bearer (JWT) Authentication (bearer):
```python
import time
import butler
from butler.api import models_api
from butler.model.put_document_labels_dto import PutDocumentLabelsDto
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
    api_instance = models_api.ModelsApi(api_client)
    id = "id_example" # str | The id of the model.
    document_id = "documentId_example" # str | The id of the document.
    put_document_labels_dto = PutDocumentLabelsDto(
        fields=[
            SimpleFieldWithConfidenceLabeledResultDto(
                id="id_example",
                name="name_example",
                type=ModelFieldType("Text"),
                confidence_score=DocExConfidence("High"),
                blocks=[
                    BlockDto(
                        id="id_example",
                        block_type=BlockType("Word"),
                        text="text_example",
                        bounding_box=,
                    ),
                ],
                region=,
                value="value_example",
            ),
        ],
        signatures=[
            SignatureFieldWithConfidenceLabeledResultDto(
                id="id_example",
                name="name_example",
                type=ModelFieldType("Text"),
                confidence_score=DocExConfidence("High"),
                region=,
                value="value_example",
            ),
        ],
        tables=[
            TrainingTableWithConfidenceLabeledResultDto(
                id="id_example",
                name="name_example",
                type=ModelFieldType("Text"),
                confidence_score=DocExConfidence("High"),
                columns=[
                    TrainingColumnDto(
                        id="id_example",
                        name="name_example",
                    ),
                ],
                rows=[
                    TrainingRowWithConfidenceLabeledResultDto(
                        id="id_example",
                        cells=[
                            TrainingCellWithConfidenceLabeledResultDto(
                                column_id="column_id_example",
                                confidence_score=DocExConfidence("High"),
                                blocks=[
                                    BlockDto(
                                        id="id_example",
                                        block_type=BlockType("Word"),
                                        text="text_example",
                                        bounding_box=,
                                    ),
                                ],
                                region=,
                                value="value_example",
                            ),
                        ],
                    ),
                ],
            ),
        ],
        overwrite=True,
    ) # PutDocumentLabelsDto | 

    # example passing only required values which don't have defaults set
    try:
        # Update labels for a specific document
        api_instance.update_document_labels(id, document_id, put_document_labels_dto)
    except butler.ApiException as e:
        print("Exception when calling ModelsApi->update_document_labels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the model. |
 **document_id** | **str**| The id of the document. |
 **put_document_labels_dto** | [**PutDocumentLabelsDto**](PutDocumentLabelsDto.md)|  |

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns successful if the labels are updated correctly |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

