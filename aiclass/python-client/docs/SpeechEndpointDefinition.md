# SpeechEndpointDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrent_recognitions** | **int** | The number of concurrent recognitions the endpoint supports. | [optional] 
**content_logging_enabled** | **bool** | A value indicating whether content logging (audio &amp;amp; transcriptions) is being used for a deployment. | [optional] 
**models** | [**list[ModelIdentity]**](ModelIdentity.md) | Information about the deployed models. | 
**description** | **str** | The description of the object. | [optional] 
**locale** | **str** | The locale of the contained data. | 
**properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
**name** | **str** | The name of the object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


