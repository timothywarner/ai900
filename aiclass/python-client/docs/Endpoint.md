# Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrent_recognitions** | **int** | The number of concurrent recognitions the endpoint supports. | [optional] 
**id** | **str** | The identifier of this entity. | 
**name** | **str** | The name of the object. | 
**description** | **str** | The description of the object. | [optional] 
**endpoint_urls** | **dict(str, str)** | The list of endpoint urls. | [optional] 
**endpoint_kind** | **str** | The kind of this endpoint (e.g. custom speech). | 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**status** | **str** | The status of the object. | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**content_logging_enabled** | **bool** | A value indicating whether content logging (audio &amp;amp; transcriptions) is being used for a deployment. | [optional] 
**models** | [**list[Model]**](Model.md) | Information about the deployed models. | 
**locale** | **str** | The locale of the contained data. | 
**properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


