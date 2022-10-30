from typing import Optional

from butler.common.file_utils import infer_file_name, infer_mime_type
from butler.common.http_utils import verify_response_or_raise
from butler.common.types import EmptyJsonBody
from butler.generated.api.queues import extract_document
from butler.generated.client import AuthenticatedClient
from butler.generated.models import ExtractDocumentMultipartData, ExtractionResultsDto
from butler.generated.types import File


class PredictionsClient:
    _client: AuthenticatedClient

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
