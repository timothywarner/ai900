# swagger_client.CustomSpeechDatasetsForModelAdaptationApi

All URIs are relative to *https://eastus.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#delete_dataset) | **DELETE** /api/speechtotext/v2.0/datasets/{id} | Deletes the specified dataset.
[**get_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset) | **GET** /api/speechtotext/v2.0/datasets/{id} | Gets the dataset identified by the given ID.
[**get_datasets**](CustomSpeechDatasetsForModelAdaptationApi.md#get_datasets) | **GET** /api/speechtotext/v2.0/datasets | Gets a list of datasets for the authenticated subscription.
[**get_supported_locales_for_datasets**](CustomSpeechDatasetsForModelAdaptationApi.md#get_supported_locales_for_datasets) | **GET** /api/speechtotext/v2.0/datasets/locales | Gets a list of supported locales for data imports.
[**update_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#update_dataset) | **PATCH** /api/speechtotext/v2.0/datasets/{id} | Updates the mutable details of the dataset identified by its ID.
[**upload_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#upload_dataset) | **POST** /api/speechtotext/v2.0/datasets/upload | Uploads data and creates a new dataset.


# **delete_dataset**
> delete_dataset(id)

Deletes the specified dataset.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.

try:
    # Deletes the specified dataset.
    api_instance.delete_dataset(id)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->delete_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(id)

Gets the dataset identified by the given ID.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.

try:
    # Gets the dataset identified by the given ID.
    api_response = api_instance.get_dataset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> list[Dataset] get_datasets()

Gets a list of datasets for the authenticated subscription.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of datasets for the authenticated subscription.
    api_response = api_instance.get_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dataset]**](Dataset.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_datasets**
> IReadOnlyDictionary2 get_supported_locales_for_datasets()

Gets a list of supported locales for data imports.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of supported locales for data imports.
    api_response = api_instance.get_supported_locales_for_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_supported_locales_for_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IReadOnlyDictionary2**](IReadOnlyDictionary2.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(id, dataset_update)

Updates the mutable details of the dataset identified by its ID.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the dataset.
dataset_update = swagger_client.DatasetUpdate() # DatasetUpdate | The updated values for the dataset.

try:
    # Updates the mutable details of the dataset identified by its ID.
    api_response = api_instance.update_dataset(id, dataset_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->update_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **dataset_update** | [**DatasetUpdate**](DatasetUpdate.md)| The updated values for the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset**
> upload_dataset(name=name, description=description, locale=locale, data_import_kind=data_import_kind, properties=properties, audiodata=audiodata, transcriptions=transcriptions, languagedata=languagedata)

Uploads data and creates a new dataset.

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
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of this data import (always add this string for any import). (optional)
description = 'description_example' # str | Optional description of this data import. (optional)
locale = 'locale_example' # str | The locale of this data import (always add this string for any import). (optional)
data_import_kind = 'data_import_kind_example' # str | The kind of the data import (always add this string for any import). (optional)
properties = 'properties_example' # str | Optional properties of this data import (json serialized object with key/values, where all values must be strings) (optional)
audiodata = '/path/to/file.txt' # file | A zip file containing the audio data (this and the audio archive file for acoustic data imports). (optional)
transcriptions = '/path/to/file.txt' # file | A text file containing the transcriptions for the audio data (this and the transcriptions file for acoustic data imports). (optional)
languagedata = '/path/to/file.txt' # file | A text file containing the language or pronunciation data (only this file for language data imports). (optional)

try:
    # Uploads data and creates a new dataset.
    api_instance.upload_dataset(name=name, description=description, locale=locale, data_import_kind=data_import_kind, properties=properties, audiodata=audiodata, transcriptions=transcriptions, languagedata=languagedata)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->upload_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of this data import (always add this string for any import). | [optional] 
 **description** | **str**| Optional description of this data import. | [optional] 
 **locale** | **str**| The locale of this data import (always add this string for any import). | [optional] 
 **data_import_kind** | **str**| The kind of the data import (always add this string for any import). | [optional] 
 **properties** | **str**| Optional properties of this data import (json serialized object with key/values, where all values must be strings) | [optional] 
 **audiodata** | **file**| A zip file containing the audio data (this and the audio archive file for acoustic data imports). | [optional] 
 **transcriptions** | **file**| A text file containing the transcriptions for the audio data (this and the transcriptions file for acoustic data imports). | [optional] 
 **languagedata** | **file**| A text file containing the language or pronunciation data (only this file for language data imports). | [optional] 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

