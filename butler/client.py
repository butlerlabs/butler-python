import logging
from typing import List, Optional

from butler.annotations.annotations import Annotations
from butler.generated.api.models import get_model, get_training_document, get_training_documents
from butler.generated.api.queues import extract_document
from butler.generated.client import AuthenticatedClient
from butler.generated.models import (
    ExtractDocumentMultipartData,
    ExtractionResultsDto,
    PaginatedTrainingDocumentsDto,
    TrainingDocumentResultDto,
)
from butler.generated.models.model_training_document_status import ModelTrainingDocumentStatus
from butler.generated.types import File
from butler.utils import EmptyJsonBody, infer_file_name, infer_mime_type, verify_response_or_raise


class Client:
    def __init__(self, api_key: str, base_url: Optional[str] = None) -> None:
        self._client = AuthenticatedClient(
            base_url=base_url if base_url is not None else "https://app.butlerlabs.ai",
            token=api_key,
            timeout=60.0,
        )

    def extract_document(
        self,
        queue_id: str,
        file_path: str,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
    ) -> ExtractionResultsDto:
        """
        Uploads a supported file (PDF, PNG, and JPG) to the Butler API and fetches results

        Limitations: Function times out in 30 seconds, works on PDFs of sizes up to 5 pages
        """
        with open(file_path, "rb") as f:
            file_name = file_name if file_name is not None else infer_file_name(f)
            mime_type = mime_type if mime_type is not None else infer_mime_type(file_name)
            return verify_response_or_raise(
                extract_document.sync_detailed(
                    client=self._client,
                    queue_id=queue_id,
                    multipart_data=ExtractDocumentMultipartData(
                        file=File(
                            payload=f,
                            file_name=file_name,
                            mime_type=mime_type,
                        ),
                    ),
                    json_body=EmptyJsonBody(),
                )
            )

    def _get_training_documents(
        self,
        model_id: str,
        after_id: Optional[str],
        document_status: ModelTrainingDocumentStatus = ModelTrainingDocumentStatus.LABELED,
    ) -> PaginatedTrainingDocumentsDto:
        return verify_response_or_raise(
            get_training_documents.sync_detailed(
                client=self._client, id=model_id, after_id=after_id, document_status=document_status
            )
        )

    def load_annotations(
        self,
        model_id: str,
        load_all_pages: bool = False,
        document_status: ModelTrainingDocumentStatus = ModelTrainingDocumentStatus.LABELED,
    ) -> Annotations:
        """
        Loads annotations from a model using the Butler API
        """
        # First load the model details so the schema can be passed to the Annotations object
        logging.info("Loading model details")
        model_details = verify_response_or_raise(get_model.sync_detailed(client=self._client, id=model_id))

        training_docs_list: List[TrainingDocumentResultDto] = []

        should_fetch_more_docs = True
        after_id = None
        logging.info("Loading training documents")
        while should_fetch_more_docs:
            # Fetch the next batch of training documents
            training_docs_page = self._get_training_documents(model_id, after_id, document_status=document_status)

            # Get details for each training document, which includes the annotations
            for training_doc in training_docs_page.items:
                training_doc_details = verify_response_or_raise(
                    get_training_document.sync_detailed(
                        client=self._client,
                        id=model_id,
                        document_id=training_doc.document_id,
                    ),
                )
                training_docs_list.append(training_doc_details)

            logging.info("Loaded %d of %d training documents", len(training_docs_list), training_docs_page.total_count)

            # Determine if we should fetch more documents
            after_id = training_docs_page.items[-1].document_id
            should_fetch_more_docs = load_all_pages and training_docs_page.has_next

        logging.info("Creating Annotations")
        return Annotations(
            model_details=model_details,
            training_documents=training_docs_list,
        )
