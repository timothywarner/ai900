# swagger_client.CustomSpeechEndpointsApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoint**](CustomSpeechEndpointsApi.md#create_endpoint) | **POST** /api/speechtotext/v2.0/endpoints | Creates a new endpoint.
[**create_endpoint_data_export**](CustomSpeechEndpointsApi.md#create_endpoint_data_export) | **POST** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Create a new endpoint data export task.
[**delete_endpoint**](CustomSpeechEndpointsApi.md#delete_endpoint) | **DELETE** /api/speechtotext/v2.0/endpoints/{id} | Deletes the endpoint identified by the given ID.
[**delete_endpoint_data**](CustomSpeechEndpointsApi.md#delete_endpoint_data) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Deletes the transcriptions and captured audio files associated with the endpoint identified by the given ID.
[**delete_endpoint_data_export**](CustomSpeechEndpointsApi.md#delete_endpoint_data_export) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Deletes the endpoint data export task identified by the given ID.
[**get_endpoint**](CustomSpeechEndpointsApi.md#get_endpoint) | **GET** /api/speechtotext/v2.0/endpoints/{id} | Gets the endpoint identified by the given ID.
[**get_endpoint_data_export**](CustomSpeechEndpointsApi.md#get_endpoint_data_export) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Gets the specified endpoint data export task for the authenticated user.
[**get_endpoint_data_exports**](CustomSpeechEndpointsApi.md#get_endpoint_data_exports) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Gets the list of endpoint data export tasks for the authenticated user.
[**get_endpoints**](CustomSpeechEndpointsApi.md#get_endpoints) | **GET** /api/speechtotext/v2.0/endpoints | Gets the list of endpoints for the authenticated subscription.
[**get_supported_locales_for_endpoints**](CustomSpeechEndpointsApi.md#get_supported_locales_for_endpoints) | **GET** /api/speechtotext/v2.0/endpoints/locales | Gets a list of supported locales for endpoint creations.
[**update_endpoint**](CustomSpeechEndpointsApi.md#update_endpoint) | **PATCH** /api/speechtotext/v2.0/endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.


# **create_endpoint**
> create_endpoint(endpoint_definition)

Creates a new endpoint.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_definition = swagger_client.SpeechEndpointDefinition() # SpeechEndpointDefinition | The details of the endpoint.

try:
    # Creates a new endpoint.
    api_instance.create_endpoint(endpoint_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->create_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_definition** | [**SpeechEndpointDefinition**](SpeechEndpointDefinition.md)| The details of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint_data_export**
> ErrorContent create_endpoint_data_export(endpoint_id, endpoint_data_definition)

Create a new endpoint data export task.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | The identifier of the endpoint.
endpoint_data_definition = swagger_client.EndpointDataDefinition() # EndpointDataDefinition | The details of the new endpoint data export.

try:
    # Create a new endpoint data export task.
    api_response = api_instance.create_endpoint_data_export(endpoint_id, endpoint_data_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->create_endpoint_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | [**str**](.md)| The identifier of the endpoint. | 
 **endpoint_data_definition** | [**EndpointDataDefinition**](EndpointDataDefinition.md)| The details of the new endpoint data export. | 

### Return type

[**ErrorContent**](ErrorContent.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint**
> delete_endpoint(id)

Deletes the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.

try:
    # Deletes the endpoint identified by the given ID.
    api_instance.delete_endpoint(id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->delete_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_data**
> delete_endpoint_data(endpoint_id)

Deletes the transcriptions and captured audio files associated with the endpoint identified by the given ID.

Deletion will happen in the background and can take up to a day.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | The identifier of the endpoint.

try:
    # Deletes the transcriptions and captured audio files associated with the endpoint identified by the given ID.
    api_instance.delete_endpoint_data(endpoint_id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->delete_endpoint_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_data_export**
> delete_endpoint_data_export(endpoint_id, id)

Deletes the endpoint data export task identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | The identifier of the endpoint.
id = 'id_example' # str | The identifier of the endpoint data export.

try:
    # Deletes the endpoint data export task identified by the given ID.
    api_instance.delete_endpoint_data_export(endpoint_id, id)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->delete_endpoint_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | [**str**](.md)| The identifier of the endpoint. | 
 **id** | [**str**](.md)| The identifier of the endpoint data export. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint**
> Endpoint get_endpoint(id)

Gets the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.

try:
    # Gets the endpoint identified by the given ID.
    api_response = api_instance.get_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->get_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_data_export**
> EndpointData get_endpoint_data_export(endpoint_id, id)

Gets the specified endpoint data export task for the authenticated user.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | The identifier of the endpoint.
id = 'id_example' # str | The identifier of the data export.

try:
    # Gets the specified endpoint data export task for the authenticated user.
    api_response = api_instance.get_endpoint_data_export(endpoint_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->get_endpoint_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | [**str**](.md)| The identifier of the endpoint. | 
 **id** | [**str**](.md)| The identifier of the data export. | 

### Return type

[**EndpointData**](EndpointData.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_data_exports**
> list[EndpointData] get_endpoint_data_exports(endpoint_id)

Gets the list of endpoint data export tasks for the authenticated user.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | The identifier of the endpoint.

try:
    # Gets the list of endpoint data export tasks for the authenticated user.
    api_response = api_instance.get_endpoint_data_exports(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->get_endpoint_data_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | [**str**](.md)| The identifier of the endpoint. | 

### Return type

[**list[EndpointData]**](EndpointData.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints**
> list[Endpoint] get_endpoints()

Gets the list of endpoints for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Gets the list of endpoints for the authenticated subscription.
    api_response = api_instance.get_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->get_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Endpoint]**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_endpoints**
> list[str] get_supported_locales_for_endpoints()

Gets a list of supported locales for endpoint creations.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for endpoint creations.
    api_response = api_instance.get_supported_locales_for_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->get_supported_locales_for_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint**
> Endpoint update_endpoint(id, endpoint_update)

Updates the metadata of the endpoint identified by the given ID.

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
api_instance = swagger_client.CustomSpeechEndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the endpoint.
endpoint_update = swagger_client.EndpointMetadataUpdate() # EndpointMetadataUpdate | The updated values for the endpoint.

try:
    # Updates the metadata of the endpoint identified by the given ID.
    api_response = api_instance.update_endpoint(id, endpoint_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechEndpointsApi->update_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the endpoint. | 
 **endpoint_update** | [**EndpointMetadataUpdate**](EndpointMetadataUpdate.md)| The updated values for the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

