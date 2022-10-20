# TrainingTableWithConfidenceLabeledResultDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of this table. | 
**name** | **str** | The name of the table. | 
**type** | [**ModelFieldType**](ModelFieldType.md) |  | 
**confidence_score** | [**DocExConfidence**](DocExConfidence.md) |  | 
**columns** | [**[TrainingColumnDto]**](TrainingColumnDto.md) | The columns for this table. | 
**rows** | [**[TrainingRowWithConfidenceLabeledResultDto]**](TrainingRowWithConfidenceLabeledResultDto.md) | The rows and labeled results for this table. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


