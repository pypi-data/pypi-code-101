# -*- coding: utf-8 -*-
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

import uuid

from fhir.resources.claim import Claim
from fhir.resources import backboneelement, domainresource
from enum import Enum, unique

from typing import List, Tuple


@unique
class InsightType(str, Enum):
    NotApplicable       = "Not Applicable"
    ClaimLineValid      = "Claim Line Valid"
    ClaimNotPayable     = "Claim Not Payable"
    ClaimPartialPayable = "Claim Partially Payable"
    ClaimLineNotPayable = "Claim Line Not Payable"
    RecodeClaimLine     = "Recode Claim Line"
    AdjustPayment       = "Adjust Payment"
    ManualReview        = "Manual Review"
    Error               = "Error"


class TranslatedMessage(domainresource.DomainResource):
    """TranslatedMessage.
    """

    resource_type = Field("TranslatedMessage", const=True)
    lang: str = Field(
        None,
        alias="lang",
        title="Language",
        description=(
            "In most cases 'en'"
        ),
        # if property is element of this resource.
        element_property=True,
    )
    message: str = Field(
        None,
        alias="message",
        title="Defensibility message",
        description=(
            "This should explain why the engine provided this insight. "
            "In most cases should include links to reference documents, policies, plans, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class MessageBundle(domainresource.DomainResource):
    """MessageBundle .
    """

    resource_type = Field("MessageBundle", const=True)

    uuid: str = Field(
        None,
        alias="uuid",
        title="Unique identifier of the defensibility statement",
        description=(
            "It should be stable. Each time you get the same insight, you receive the same uuid here."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    messages: List[TranslatedMessage] = Field(
        None,
        alias="messages",
        title="List of translated defensibility messages",
        description=(
            "Usually the language is 'en'."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class Defense(domainresource.DomainResource):
    """Defense provides some backing support information for the proposed change.
    """

    resource_type = Field("Defense", const=True)
    script: MessageBundle = Field(
        None,
        alias="script",
        title="A collection of defensibility messages",
        description=(
            "This should explain why the engine provided this insight. "
            "In most cases should include links to reference documents, policies, plans, etc."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    referenceData: List[str] = Field("referenceData")


class Trace(domainresource.DomainResource):
    """When a claim line is evaluated, it causes a certain path to be traversed
    in a decision tree. For one such decision tree, this class holds the data
    about this path. More specifically, the predicates in the nodes encountered
    during the traversal of the tree, and what answer (YES/NO) was obtained for
    each such predicate."""

    resource_type = Field("Trace", const=True)

    tree_name: str = Field(
        default=None,
        alias='tree_name',
        description='The name of the tree that has the predicates listed in this trace.'
    )
    traversal: List[Tuple[str, ...]] = Field(
        default_factory=lambda: list(),
        alias='traversal',
        description='The actual list of predicates and their respective answers. Each item is a '
                    'tuple of strings. The first string should be the predicate question, and the '
                    'second string, the respective answer. If more strings are present in a tuple '
                    'they can contain additional information, like node label, etc.'
    )
    end_label: str = Field(
        default=None,
        alias='end_label',
        description='The label of the end-node that was reached after the last predicate was evaluated.'
    )


class Insight(domainresource.DomainResource):
    """Insight is the result of running an insight engine on a claim.

    Typically insight is a result of evaluating of a single claim line.
    """

    resource_type = Field("Insight", const=True)

    id: str = Field(None, alias="id")
    type: InsightType = Field(InsightType.Error, alias="type", description="Insight type is used in recommendation engine to order all available insights")
    description: str = Field(None, alias="description")
    defense: Defense = Field(None, alias="defense")
    action: str = Field(None, alias="action", description=("Action is a formal string in Java Script that describes the intended change"))
    trace: List[Trace] = Field(None, alias='trace')
    policy_name: str = Field(None, alias='policy_name')
    claim_line_sequence_num: int = Field(0, alias="claimLineSequenceNum", description="If the insight is for claim line, then this property is sequence num of the respective line")
    error_code: int = Field(0, alias="errorCode", description="If insight type is Error, this property contains error code that is to be reported to engine developer")


class InsightEngineResponse(domainresource.DomainResource):
    """Insight Engine response.

    Response contains the insights.
    """

    resource_type = Field("InsightEngineResponse", const=True)

    engine_name: str = Field(None, alias='engine_name')
    insights: List[Insight] = Field(
        None,
        alias="insights",
        title="List of insights produced by this engine",
        description=(
            "Usually each claim line produces a single insight. "
            "Sometimes however, there might be 0 or more insights."
        ),
        # if property is element of this resource.
        element_property=True,
    )


