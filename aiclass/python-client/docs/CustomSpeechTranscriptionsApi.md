# swagger_client.CustomSpeechTranscriptionsApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transcription**](CustomSpeechTranscriptionsApi.md#create_transcription) | **POST** /api/speechtotext/v2.0/transcriptions | Creates a new transcription.
[**delete_transcription**](CustomSpeechTranscriptionsApi.md#delete_transcription) | **DELETE** /api/speechtotext/v2.0/transcriptions/{id} | Deletes the specified transcription task.
[**get_supported_locales_for_transcriptions**](CustomSpeechTranscriptionsApi.md#get_supported_locales_for_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions/locales | Gets a list of supported locales for offline transcriptions.
[**get_transcription**](CustomSpeechTranscriptionsApi.md#get_transcription) | **GET** /api/speechtotext/v2.0/transcriptions/{id} | Gets the transcription identified by the given ID.
[**get_transcriptions**](CustomSpeechTranscriptionsApi.md#get_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions | Gets a list of transcriptions for the authenticated subscription.
[**update_transcription**](CustomSpeechTranscriptionsApi.md#update_transcription) | **PATCH** /api/speechtotext/v2.0/transcriptions/{id} | Updates the mutable details of the transcription identified by its ID.


# **create_transcription**
> create_transcription(transcription)

Creates a new transcription.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
transcription = swagger_client.TranscriptionDefinition() # TranscriptionDefinition | The details of the new transcription.

try:
    # Creates a new transcription.
    api_instance.create_transcription(transcription)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->create_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription** | [**TranscriptionDefinition**](TranscriptionDefinition.md)| The details of the new transcription. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transcription**
> ErrorContent delete_transcription(id)

Deletes the specified transcription task.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.

try:
    # Deletes the specified transcription task.
    api_response = api_instance.delete_transcription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->delete_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 

### Return type

[**ErrorContent**](ErrorContent.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_transcriptions**
> list[str] get_supported_locales_for_transcriptions()

Gets a list of supported locales for offline transcriptions.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for offline transcriptions.
    api_response = api_instance.get_supported_locales_for_transcriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->get_supported_locales_for_transcriptions: %s\n" % e)
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

# **get_transcription**
> Transcription get_transcription(id)

Gets the transcription identified by the given ID.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.

try:
    # Gets the transcription identified by the given ID.
    api_response = api_instance.get_transcription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->get_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcriptions**
> list[Transcription] get_transcriptions(skip=skip, take=take)

Gets a list of transcriptions for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Number of transcriptions that will be skipped. (optional)
take = 56 # int | Number of transcriptions that will be included after skipping. (optional)

try:
    # Gets a list of transcriptions for the authenticated subscription.
    api_response = api_instance.get_transcriptions(skip=skip, take=take)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->get_transcriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of transcriptions that will be skipped. | [optional] 
 **take** | **int**| Number of transcriptions that will be included after skipping. | [optional] 

### Return type

[**list[Transcription]**](Transcription.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transcription**
> Transcription update_transcription(id, transcription_update)

Updates the mutable details of the transcription identified by its ID.

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
api_instance = swagger_client.CustomSpeechTranscriptionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the transcription.
transcription_update = swagger_client.TranscriptionUpdate() # TranscriptionUpdate | The updated values for the transcription.

try:
    # Updates the mutable details of the transcription identified by its ID.
    api_response = api_instance.update_transcription(id, transcription_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechTranscriptionsApi->update_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the transcription. | 
 **transcription_update** | [**TranscriptionUpdate**](TranscriptionUpdate.md)| The updated values for the transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

