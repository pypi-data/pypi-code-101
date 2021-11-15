# pylint: disable=line-too-long, bad-indentation, trailing-whitespace

from typing import Optional, TextIO, Tuple

from cocluremig.visualization.dot_base_writer import BaseDotWriter


class PrettyDotWriter(BaseDotWriter):
    """
    Human readable dot file with indents and line-breaks
    """

    def __init__(self, file_writer: TextIO):
        BaseDotWriter.__init__(self, file_writer)

    def write_head(self, name: str):
        BaseDotWriter.write_head(self, name)
        self._file_writer.write("\n")

    def write_edge(self, edge: Tuple[str, str]):
        self._file_writer.write("\t")
        BaseDotWriter.write_edge(self, edge)
        self._file_writer.write("\n")

    def write_vertex(self, vertex: str, label: Optional[str] = None, color: Optional[str] = None):
        self._file_writer.write("\t")
        BaseDotWriter.write_vertex(self, vertex, label, color)
        self._file_writer.write("\n")
