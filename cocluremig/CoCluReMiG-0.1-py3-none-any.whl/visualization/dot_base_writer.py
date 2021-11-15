from typing import Optional, TextIO, Tuple

from cocluremig.utils.gitutils import normalize_id_name


class BaseDotWriter:
    """
    Base class for dot-File-Writing
    """

    def __init__(self, file_writer: TextIO):
        """
        Creates the dot writer

        @param file_writer: a file-writer to write the dot-file into
        """
        self._file_writer = file_writer
        self.__closed = False

    def write_head(self, name: str):
        """
        writes header

        @param name: graph name
        """
        self._file_writer.write(" digraph ")
        self._file_writer.write(normalize_id_name(name))
        self._file_writer.write(" {")

    def write_edge(self, edge: Tuple[str, str]):
        """
        writes an edge

        @param edge: edge to write
        """
        (v1, v2) = edge
        self._file_writer.write("\"")
        self._file_writer.write(v1)
        self._file_writer.write("\" -> \"")
        self._file_writer.write(v2)
        self._file_writer.write("\"; ")

    def write_vertex(self, vertex: str, label: Optional[str] = None, color: Optional[str] = None):
        """
        writes a vertex to the graph

        @param vertex: the vertex to write
        @param label: a label to use instead of identifier
        @param color: a color for the vertex
        """
        self._file_writer.write("\"")
        self._file_writer.write(vertex)
        self._file_writer.write("\"")
        if [x for x in [label, color] if x]:
            self._file_writer.write(" [")
            if label:
                self._file_writer.write("label=\"")
                self._file_writer.write(label)
                self._file_writer.write("\"")
            if label and color:
                self._file_writer.write(",")
            if color:
                self._file_writer.write("color=\"")
                self._file_writer.write(color)
                self._file_writer.write("\"")
            self._file_writer.write("]")
        self._file_writer.write("; ")

    def write_footer(self):
        """
        writes footer
        """
        self._file_writer.write("}")

    def close(self):
        """
        closes the file
        """
        self._file_writer.flush()
        self.__closed = True

    def __del__(self):
        if not self.__closed:
            self.close()
        self._file_writer.close()
