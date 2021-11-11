from enum import Enum
from typing import List, Optional
from .common import ClientObject


class LabelConfigType(Enum):
    IMAGE_CLASSIFICATION = 'image_classification'
    TEXT_CLASSIFICATION = 'text_classification'
    IMAGE_SEGMENTATION = 'image_segmentation'
    OBJECT_DETECTION = 'object_detection'
    TEXT_TAGGING = 'text_tagging'


class LabelConfig(ClientObject):

    labels: List[str] = []
    type: Optional[LabelConfigType] = None
    xml_string: str = ''

    def get_data_fields(self):
        response = self.client.make_request(method='GET', url=f'/api/projects/{self.id}/label-config')
