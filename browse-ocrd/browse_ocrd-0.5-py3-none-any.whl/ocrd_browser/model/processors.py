import json
from collections import defaultdict
from typing import Dict, Any, List

from ocrd_validators.constants import OCRD_TOOL_SCHEMA


class Processors:

    def __init__(self, processor_data: Dict[str, Any]):
        tool_properties = OCRD_TOOL_SCHEMA['properties']['tools']['patternProperties']['ocrd-.*']['properties']

        self.processors_by_step: Dict[str, List[str]] = defaultdict(list)
        for step in tool_properties['steps']['items']['enum']:
            self.processors_by_step[step] = []

        self.processors_by_category: Dict[str, List[str]] = defaultdict(list)
        for category in tool_properties['categories']['items']['enum']:
            self.processors_by_category[category] = []

        for key, processor in processor_data.items():
            for category in processor['tool_json']['categories']:
                self.processors_by_category[category].append(key)
            for step in processor['tool_json']['steps']:
                self.processors_by_step[step].append(key)

    def get_processors_by_category(self) -> Dict[str, List[str]]:
        return self.processors_by_category

    @staticmethod
    def load_processor_info(filename: str = '/home/jk/PycharmProjects/ocrd-environment/ocrd_environment/ocrd-tools.json') -> 'Processors':
        with open(filename, mode='r') as fp:
            return Processors(json.load(fp))
