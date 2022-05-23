# ExtractionResultsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document | 
**document_status** | [**DocumentStatus**](DocumentStatus.md) |  | 
**file_name** | **str** | Name of the uploaded file | 
**mime_type** | **str** | Mime Type of the uploaded file | 
**document_type** | **str** | Name of the document type | 
**confidence_score** | [**DocExConfidence**](DocExConfidence.md) |  | [optional] 
**extraction_range** | **object** | Range of pages that extraction ran on. Only populated if the document was filtered | [optional] 
**form_fields** | [**[ExtractedFieldDto]**](ExtractedFieldDto.md) | Extracted form fields of this document. May be undefined if extraction not completed | [optional] 
**tables** | [**[ExtractedTableDto]**](ExtractedTableDto.md) | Extracted tables of this document. May be undefined if extraction not completed | [optional] 
**extra_results** | **object** | Any \&quot;extra\&quot; results from extraction. These are lower-level results that you can use to implement extra post-processing logic, if needed. These are only available if the \&quot;extra_results\&quot; query parameter was set | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


