from typing import Optional

from butler.annotations import AnnotationsClient
from butler.generated.client import AuthenticatedClient
from butler.predictions import PredictionsClient


class Client(PredictionsClient, AnnotationsClient):
    def __init__(self, api_key: str, base_url: Optional[str] = None) -> None:
        self._client = AuthenticatedClient(
            base_url=base_url if base_url is not None else "https://app.butlerlabs.ai",
            token=api_key,
            timeout=60.0,
        )
