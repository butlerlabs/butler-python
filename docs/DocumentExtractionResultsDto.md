# DocumentExtractionResultsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the document | 
**file_name** | **str** |  | 
**mime_type** | **str** |  | 
**document_type** | **str** |  | 
**extracted_fields** | [**[ExtractedFieldDto]**](ExtractedFieldDto.md) |  | 
**tables** | [**[ExtractedTableDto]**](ExtractedTableDto.md) |  | 
**confidence_score** | [**DocExConfidence**](DocExConfidence.md) |  | 
**extraction_range** | **object** | Page range that extraction ran on. Only populated if the document was filtered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


