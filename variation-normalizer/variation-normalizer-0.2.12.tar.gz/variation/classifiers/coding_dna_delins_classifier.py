"""A module for the Coding DNA DelIns Classifier."""
from typing import List
from .set_based_classifier import SetBasedClassifier
from variation.schemas.classification_response_schema import ClassificationType


class CodingDNADelInsClassifier(SetBasedClassifier):
    """The Coding DNA DelIns Classifier class."""

    def classification_type(self) -> ClassificationType:
        """Return the Coding DNA DelIns classification type."""
        return ClassificationType.CODING_DNA_DELINS

    def exact_match_candidates(self) -> List[List[str]]:
        """Return the exact match token type candidates."""
        return [
            ['CodingDNADelIns'],
            ['GeneSymbol', 'AminoAcidSubstitution', 'CodingDNADelIns'],
            ['CodingDNADelIns', 'GeneSymbol'],
            ['GeneSymbol', 'CodingDNADelIns'],
            ['HGVS', 'CodingDNADelIns'],
            ['ReferenceSequence', 'CodingDNADelIns'],
            ['LocusReferenceGenomic', 'CodingDNADelIns']
        ]
