import logging
from typing import List

from butler.annotations.document_annotation_with_image import DocumentAnnotationWithImage
from butler.annotations.ner_utils import DocumentNerAnnotation, document_annotation_to_ner
from butler.generated.models import ModelInfoDto, TrainingDocumentResultDto


class Annotations:
    """
    This class represents the annotations for a dataset that can be
    used to train a document extraction model.
    """

    model_details: ModelInfoDto
    training_documents: List[DocumentAnnotationWithImage]

    def __init__(
        self,
        model_details: ModelInfoDto,
        training_documents: List[TrainingDocumentResultDto],
    ):
        self.model_details = model_details
        self.training_documents = list(map(lambda doc: DocumentAnnotationWithImage(doc), training_documents))

    def as_ner(self, as_iob: bool = True) -> List[DocumentNerAnnotation]:
        """
        Returns the list of annotations in a common NER format.
        """
        logging.info("Converting annotations to NER format")
        return list(
            map(lambda doc: document_annotation_to_ner(self.model_details, doc, as_iob=as_iob), self.training_documents)
        )
