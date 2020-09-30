# swagger_client.ServiceHealthApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_status**](ServiceHealthApi.md#get_health_status) | **GET** /api/common/v2.0/healthstatus | The action returns the health of the different components of the serivce.


# **get_health_status**
> HealthStatusResponse get_health_status()

The action returns the health of the different components of the serivce.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ServiceHealthApi(swagger_client.ApiClient(configuration))

try:
    # The action returns the health of the different components of the serivce.
    api_response = api_instance.get_health_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceHealthApi->get_health_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthStatusResponse**](HealthStatusResponse.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

