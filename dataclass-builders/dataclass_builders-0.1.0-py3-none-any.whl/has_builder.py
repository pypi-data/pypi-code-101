from typing import Any

from dataclass_builder.builder import Builder


class HasBuilder:
    """Abstract class that endows children with Builders"""

    @classmethod
    def Builder(cls, **kwargs: Any) -> Builder:
        return Builder(cls, **kwargs)
