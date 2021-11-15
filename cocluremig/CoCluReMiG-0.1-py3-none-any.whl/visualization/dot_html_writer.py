import os
from typing import Iterable, Optional, TextIO, Tuple

from cocluremig.utils.gitutils import normalize_id_name
from cocluremig.visualization.dot_writer import BaseDotWriter
from pynpmd import JsLibResolver


class DotHtmlRenderWriter(BaseDotWriter):
    """
    html-based dot-based view using d3-graphviz
    """

    def __init__(self, file_writer: TextIO):
        BaseDotWriter.__init__(self, file_writer)
        self._libs: Iterable[str] = []

    # noinspection PyArgumentEqualDefault
    def __dep_resolve(self):
        modules = ["jquery", "d3", "@hpcc-js/wasm", "d3-graphviz"]
        rslvr = JsLibResolver("../js_npm_lib_cache", True)
        for module in modules:
            path = rslvr.get_lib(module)
            self._libs += [path]
        # store abspaths on runtime
        self._libs = map(os.path.abspath, self._libs)

    def _write_js_deps(self, inline=False):
        fw = self._file_writer
        if not self._libs:
            self.__dep_resolve()
        for lib in self._libs:
            if inline:
                fw.write("<script type='application/javascript'>")
                with open(lib, "r") as reader:
                    fw.write(reader.read())
            else:
                fw.write("<script src=\"")
                fw.write(os.path.relpath(lib, os.path.dirname(fw.name)))
                fw.write("\">")
            fw.write("</script>\n")

    def write_head(self, name: str):
        fw = self._file_writer
        fw.write("<!DOCTYPE html>\n")
        fw.write("<head>\n")
        fw.write("<meta charset=\"utf-8\">\n")
        # fw.write("<meta http-equiv=\"Content-Security-Policy\"
        # content=\"default-src *; style-src 'self'  "
        #         "'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'\">")
        fw.write("<title>")
        fw.write(normalize_id_name(name))
        fw.write("</title>\n")
        self._write_js_deps()
        fw.write("</head>\n")
        fw.write("<body>\n")

    def write_simple_render_head(self, name: str):
        """
        Write render init

        @param name: the graphs id
        """
        fw = self._file_writer
        fw.write("<div id=\"graph\" style=\"text-align: center;\"></div>\n")
        fw.write("<script>\n")
        fw.write("head = '")
        BaseDotWriter.write_head(self, name)
        fw.write("';\n")
        fw.write("data = [''+\n")

    def write_edge(self, edge: Tuple[str, str]):
        fw = self._file_writer
        fw.write("\t'")
        BaseDotWriter.write_edge(self, edge)
        fw.write("'+\n")

    def write_vertex(self, vertex: str, label: Optional[str] = None, color: Optional[str] = None):
        fw = self._file_writer
        fw.write("\t'")
        BaseDotWriter.write_vertex(self, vertex, label, color)
        fw.write("'+\n")

    def write_simple_render_foot(self):
        """
        Write render end
        """
        fw = self._file_writer
        fw.write("\t''];\n")
        fw.write("cdata = '';\n")
        fw.write("for (i=0; i<data.length; i++){\n")
        fw.write("\t")
        fw.write("cdata=cdata+data[i];\n")
        fw.write("\t")
        fw.write("console.log(i);\n\tconsole.log(data[i]);\n")
        fw.write("\t")
        fw.write("d3.select(\"#graph\").graphviz().renderDot(")
        fw.write("head+cdata+'}'")
        fw.write(");\n")
        # fw.write("}")
        # fw.write("');")
        fw.write("}\n")
        fw.write("</script>\n")

    def write_footer(self):
        fw = self._file_writer
        fw.write("</body>")
