# ModelInfoDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of this model. | 
**name** | **str** | Name of the model. | 
**status** | [**ModelStatus**](ModelStatus.md) |  | 
**model_type** | [**BaseModelType**](BaseModelType.md) |  | 
**fields** | [**[ModelFieldDto]**](ModelFieldDto.md) | The text, checkbox, and signature fields for this model | 
**tables** | [**[ModelTableDto]**](ModelTableDto.md) | The table fields for this model | 
**queue_id** | **str** | The id of the queue for this model. | 
**num_training_documents** | **float** | The number of training documents for this model | 
**training_disabled_reason** | [**TrainingDisabledReason**](TrainingDisabledReason.md) |  | [optional] 
**training_failure_reason** | **str** | Reason for previous training failure | [optional] 
**submit_training_documents_disabled_reason** | [**SubmitTrainingDocumentsDisabledReason**](SubmitTrainingDocumentsDisabledReason.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


