# swagger_client.CustomSpeechModelsApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](CustomSpeechModelsApi.md#create_model) | **POST** /api/speechtotext/v2.0/models | Creates a new model.
[**delete_model**](CustomSpeechModelsApi.md#delete_model) | **DELETE** /api/speechtotext/v2.0/models/{id} | Deletes the model identified by the given ID.
[**get_model**](CustomSpeechModelsApi.md#get_model) | **GET** /api/speechtotext/v2.0/models/{id} | Gets the model identified by the given ID.
[**get_models**](CustomSpeechModelsApi.md#get_models) | **GET** /api/speechtotext/v2.0/models | Gets the list of models for the authenticated subscription.
[**get_supported_locales_for_models**](CustomSpeechModelsApi.md#get_supported_locales_for_models) | **GET** /api/speechtotext/v2.0/models/locales | Gets a list of supported locales for model adaptation.
[**update_model**](CustomSpeechModelsApi.md#update_model) | **PATCH** /api/speechtotext/v2.0/models/{id} | Updates the metadata of the model identified by the given ID.


# **create_model**
> create_model(model_definition)

Creates a new model.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
model_definition = swagger_client.SpeechModelDefinition() # SpeechModelDefinition | The details of the new model.

try:
    # Creates a new model.
    api_instance.create_model(model_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_definition** | [**SpeechModelDefinition**](SpeechModelDefinition.md)| The details of the new model. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(id)

Deletes the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.

try:
    # Deletes the model identified by the given ID.
    api_instance.delete_model(id)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Gets the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.

try:
    # Gets the model identified by the given ID.
    api_response = api_instance.get_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> list[Model] get_models()

Gets the list of models for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))

try:
    # Gets the list of models for the authenticated subscription.
    api_response = api_instance.get_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->get_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model]**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_models**
> IReadOnlyDictionary21 get_supported_locales_for_models()

Gets a list of supported locales for model adaptation.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for model adaptation.
    api_response = api_instance.get_supported_locales_for_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->get_supported_locales_for_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IReadOnlyDictionary21**](IReadOnlyDictionary21.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> Model update_model(id, model_update)

Updates the metadata of the model identified by the given ID.

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
api_instance = swagger_client.CustomSpeechModelsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the model.
model_update = swagger_client.ModelUpdate() # ModelUpdate | The updated values for the model.

try:
    # Updates the metadata of the model identified by the given ID.
    api_response = api_instance.update_model(id, model_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechModelsApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the model. | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)| The updated values for the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

