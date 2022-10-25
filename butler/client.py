from butler.api.queues_api import QueuesApi
from butler.api.models_api import ModelsApi

from butler.api_client import ApiClient
from butler.configuration import Configuration
from butler.model.document_status import DocumentStatus
from butler.model.extraction_results_dto import ExtractionResultsDto
from butler.model.paginated_extraction_results_dto import PaginatedExtractionResultsDto

from butler.additional_models.annotations import Annotations

class Client(ApiClient):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            configuration = Configuration(
                access_token = api_key
            )
        )

    def extract_document(self, file_path: str, queue_id: str) -> ExtractionResultsDto:
        """
        Uploads a supported file (PDF, PNG, and JPG) to the Butler API and fetches results

        Limitations: Function times out in 30 seconds, works on PDFs of sizes up to 5 pages
        """
        with open(file_path, 'rb') as f:
            return QueuesApi(self).extract_document(
                queue_id = queue_id,
                file = f
            )

    def _get_training_documents(
      self,
      models_api: ModelsApi, 
      model_id: str, 
      after_id: str
    ):
      if after_id:
        return models_api.get_training_documents(
          id = model_id,
          after_id = after_id,
          _check_return_type = False
        )
      else:
        return models_api.get_training_documents(
          id = model_id,
          _check_return_type = False
        )

    def load_annotations(
      self, 
      model_id: str, 
      load_all_documents: bool = False
    ) -> Annotations:
      '''
      Loads annotations from a model using the Butler API
      '''
      models_api = ModelsApi(self)
      # First load the model details so the schema can be passed to the Annotations object
      model_details = models_api.get_model(
        id = model_id,
        _check_return_type = False
      )

      training_document_details_list = []

      should_fetch_more_docs = True
      after_id = None
      while (should_fetch_more_docs):
        # Fetch the next batch of training documents
        training_docs_response = self._get_training_documents(
          models_api,
          model_id,
          after_id
        )
        
        training_docs = training_docs_response['items']

        # Get details for each training document, which includes the annotations
        for training_doc in training_docs:
          document_id = training_doc['documentId']
          training_doc_details = models_api.get_training_document(
            id = model_id,
            document_id = document_id,
            _check_return_type = False
          )
          training_document_details_list.append(training_doc_details)

        # Determine if we should fetch more documents
        has_next = training_docs_response['has_next']
        after_id = training_docs_response['items'][-1]['documentId']
        should_fetch_more_docs = load_all_documents and has_next

      return Annotations(
        model_details = model_details,
        training_documents = training_document_details_list
      )
