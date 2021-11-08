__all__ = [
    "CompilationDatabase",
    "CompilationUnit",
]


from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple

from beet import Container, TextFile, TextFileBase
from beet.core.utils import extra_field

from .ast import AstRoot
from .diagnostic import DiagnosticCollection


@dataclass
class CompilationUnit:
    """Information associated with the compilation of a specific function file."""

    ast: Optional[AstRoot] = None
    source: Optional[str] = None
    filename: Optional[str] = None
    resource_location: Optional[str] = None

    diagnostics: DiagnosticCollection = extra_field(init=False)

    def __post_init__(self):
        self.diagnostics = DiagnosticCollection(
            filename=self.filename,
            hint=self.resource_location,
        )


class CompilationDatabase(Container[TextFileBase[Any], CompilationUnit]):
    """Compilation database."""

    index: Dict[str, TextFileBase[Any]]
    queue: List[Tuple[int, str, TextFileBase[Any]]]
    session: Set[TextFileBase[Any]]
    current: TextFileBase[Any]

    def __init__(self):
        super().__init__()
        self.index = {}
        self.queue = []
        self.session = set()
        self.current = TextFile()

    def process(
        self,
        key: TextFileBase[Any],
        value: CompilationUnit,
    ) -> CompilationUnit:
        for index in [value.filename, value.resource_location]:
            if index:
                self.index[index] = key
        value.diagnostics.file = key
        return value

    def __delitem__(self, key: TextFileBase[Any]):
        for index in [self[key].filename, self[key].resource_location]:
            if index:
                del self.index[index]
        super().__delitem__(key)

    def setup_compilation(self):
        """Setup database for compilation."""
        self.queue.clear()
        self.session.clear()

    def enqueue(self, key: TextFileBase[Any], step: int = -1):
        """Enqueue a file and schedule it to be processed with the given step."""
        heappush(self.queue, (step, self[key].resource_location or "<unknown>", key))
        self.session.add(key)

    def dequeue(self) -> Tuple[int, TextFileBase[Any]]:
        """Dequeue the next file that needs to be processed."""
        step, _, key = heappop(self.queue)
        return step, key

    def process_queue(self) -> Iterator[Tuple[int, TextFileBase[Any]]]:
        """Yield database entries from the queue."""
        while self.queue:
            step, self.current = self.dequeue()
            yield step, self.current
