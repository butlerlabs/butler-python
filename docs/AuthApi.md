# butler.AuthApi

All URIs are relative to *https://app.butlerlabs.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /api/auth | Authenticates and authorizes the user to access the API


# **login**
> login(login_body_dto)

Authenticates and authorizes the user to access the API

### Example

```python
import time
import butler
from butler.api import auth_api
from butler.model.login_body_dto import LoginBodyDto
from pprint import pprint
# Defining the host is optional and defaults to https://app.butlerlabs.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = butler.Configuration(
    host = "https://app.butlerlabs.ai"
)


# Enter a context with an instance of the API client
with butler.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_body_dto = LoginBodyDto(
        username="username_example",
        password="password_example",
    ) # LoginBodyDto | 

    # example passing only required values which don't have defaults set
    try:
        # Authenticates and authorizes the user to access the API
        api_instance.login(login_body_dto)
    except butler.ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_body_dto** | [**LoginBodyDto**](LoginBodyDto.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

