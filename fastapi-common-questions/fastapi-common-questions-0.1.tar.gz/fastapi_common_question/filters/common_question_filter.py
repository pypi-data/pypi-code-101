from typing import Any

from starlette.requests import Request

from .base_filter import get_filters
from ..schemas.common_question import CommonQuestionIn, CommonQuestionFilter
from ..models.common_question import CommonQuestion


def get_common_question_filters(*, request: Request) -> Any:
    data = dict(
        is_active=CommonQuestion.is_active,
        is_archive=CommonQuestion.is_archive,
        created_at__gt=CommonQuestion.created_at,
        created_at__lt=CommonQuestion.created_at,
        created_at=CommonQuestion.created_at,
    )
    return get_filters(request, CommonQuestionFilter, data)
