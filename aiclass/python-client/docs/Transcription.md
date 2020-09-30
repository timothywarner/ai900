# Transcription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recordings_url** | **str** |  | 
**report_file_url** | **str** |  | [optional] 
**id** | **str** | The identifier of this entity. | 
**models** | [**list[Model]**](Model.md) | The models used in this transcription. | [optional] 
**locale** | **str** | The locale of the contained data. | 
**results_urls** | **dict(str, str)** | The results Urls for the transcription. | [optional] 
**status_message** | **str** | The failure reason for the transcription. | [optional] 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**status** | **str** | The status of the object. | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**name** | **str** | The name of the object. | 
**description** | **str** | The description of the object. | [optional] 
**properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


