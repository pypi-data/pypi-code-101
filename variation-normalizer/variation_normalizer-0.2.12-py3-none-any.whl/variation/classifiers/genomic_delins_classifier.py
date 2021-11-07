"""A module for the Genomic DelIns Classifier."""
from typing import List
from .set_based_classifier import SetBasedClassifier
from variation.schemas.classification_response_schema import ClassificationType


class GenomicDelInsClassifier(SetBasedClassifier):
    """The Genomic DelIns Classifier class."""

    def classification_type(self) -> ClassificationType:
        """Return the Genomic DelIns classification type."""
        return ClassificationType.GENOMIC_DELINS

    def exact_match_candidates(self) -> List[List[str]]:
        """Return the exact match token type candidates."""
        return [
            ['GenomicDelIns'],
            ['GeneSymbol', 'AminoAcidSubstitution', 'GenomicDelIns'],
            ['GenomicDelIns', 'GeneSymbol'],
            ['GeneSymbol', 'GenomicDelIns'],
            ['HGVS', 'GenomicDelIns'],
            ['ReferenceSequence', 'GenomicDelIns']
        ]
