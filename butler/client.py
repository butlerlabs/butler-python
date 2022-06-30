from butler.api.queues_api import QueuesApi

from butler.api_client import ApiClient
from butler.configuration import Configuration
from butler.model.document_status import DocumentStatus
from butler.model.extraction_results_dto import ExtractionResultsDto
from butler.model.paginated_extraction_results_dto import PaginatedExtractionResultsDto


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
