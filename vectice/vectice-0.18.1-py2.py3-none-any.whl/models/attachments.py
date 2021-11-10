from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Tuple, Any, BinaryIO
from .with_attachments import WithAttachments


@dataclass
class Attachments(WithAttachments):
    artifact_type: Optional[str] = None
    """"""
    files: Optional[List[Tuple[str, Tuple[Any, BinaryIO]]]] = None
    """"""
