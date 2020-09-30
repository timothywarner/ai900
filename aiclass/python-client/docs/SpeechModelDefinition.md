# SpeechModelDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_kind** | **str** | The kind of this model (e.g. acoustic, language ...) | 
**text** | **str** | The text used to adapt this language model. | [optional] 
**base_model** | [**ModelIdentity**](ModelIdentity.md) | The base model used for adaptation. | [optional] 
**datasets** | [**list[DatasetIdentity]**](DatasetIdentity.md) | Datasets used for adaptation. | [optional] 
**description** | **str** | The description of the object. | [optional] 
**locale** | **str** | The locale of the contained data. | 
**properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
**name** | **str** | The name of the object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


