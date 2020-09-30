# swagger_client.CustomSpeechAccuracyTestsApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_accuracy_test**](CustomSpeechAccuracyTestsApi.md#create_accuracy_test) | **POST** /api/speechtotext/v2.0/accuracytests | Creates a new accuracy test.
[**delete_accuracy_test**](CustomSpeechAccuracyTestsApi.md#delete_accuracy_test) | **DELETE** /api/speechtotext/v2.0/accuracytests/{id} | Deletes the accuracy test identified by the given ID.
[**get_accuracy_test**](CustomSpeechAccuracyTestsApi.md#get_accuracy_test) | **GET** /api/speechtotext/v2.0/accuracytests/{id} | Gets the accuracy test identified by the given ID.
[**get_accuracy_tests**](CustomSpeechAccuracyTestsApi.md#get_accuracy_tests) | **GET** /api/speechtotext/v2.0/accuracytests | Gets the list of accuracy tests for the authenticated subscription.
[**update_accuracy_test**](CustomSpeechAccuracyTestsApi.md#update_accuracy_test) | **PATCH** /api/speechtotext/v2.0/accuracytests/{id} | Updates the mutable details of the test identified by its id.


# **create_accuracy_test**
> create_accuracy_test(test_definition)

Creates a new accuracy test.

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
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))
test_definition = swagger_client.TestDefinition() # TestDefinition | The details of the new accuracy test.

try:
    # Creates a new accuracy test.
    api_instance.create_accuracy_test(test_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->create_accuracy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_definition** | [**TestDefinition**](TestDefinition.md)| The details of the new accuracy test. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accuracy_test**
> delete_accuracy_test(id)

Deletes the accuracy test identified by the given ID.

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
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the accuracy test.

try:
    # Deletes the accuracy test identified by the given ID.
    api_instance.delete_accuracy_test(id)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->delete_accuracy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the accuracy test. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accuracy_test**
> Test get_accuracy_test(id)

Gets the accuracy test identified by the given ID.

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
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the accuracy test.

try:
    # Gets the accuracy test identified by the given ID.
    api_response = api_instance.get_accuracy_test(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->get_accuracy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the accuracy test. | 

### Return type

[**Test**](Test.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accuracy_tests**
> list[Test] get_accuracy_tests()

Gets the list of accuracy tests for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))

try:
    # Gets the list of accuracy tests for the authenticated subscription.
    api_response = api_instance.get_accuracy_tests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->get_accuracy_tests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Test]**](Test.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_accuracy_test**
> Test update_accuracy_test(id, test_update)

Updates the mutable details of the test identified by its id.

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
api_instance = swagger_client.CustomSpeechAccuracyTestsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the accuracy test.
test_update = swagger_client.TestUpdate() # TestUpdate | The object containing the updated fields of the test.

try:
    # Updates the mutable details of the test identified by its id.
    api_response = api_instance.update_accuracy_test(id, test_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechAccuracyTestsApi->update_accuracy_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the accuracy test. | 
 **test_update** | [**TestUpdate**](TestUpdate.md)| The object containing the updated fields of the test. | 

### Return type

[**Test**](Test.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

