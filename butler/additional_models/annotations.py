from typing import List

from butler.generated.models import ModelInfoDto, TrainingDocumentResultDto

"""
This class represents the annotations for a dataset that can be
used to train a document extraction model.
"""


class Annotations:
    def __init__(
        self,
        model_details: ModelInfoDto,
        training_documents: List[TrainingDocumentResultDto],
    ):
        self.model_details = model_details
        self.training_documents = training_documents

    def as_ner(self):
        raise NotImplementedError("Annotations.as_ner() is not implemented yet")
