from . import utils
from . import soup
from ..task import Task

from sphinx.util.nodes import set_source_info
from sphinx.util.docutils import SphinxDirective
from docutils import nodes



from sphinx.util import logging
_logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive('ot-taskmeta', _TaskMetaDirective)
    app.connect('doctree-resolved', _ev_doctree_resolved__expand_taskmeta_nodes)

def _ev_doctree_resolved__expand_taskmeta_nodes(app, doctree, docname):
    soup.sphinx_create_soup(app)
    for n in doctree.traverse(_TaskMetaNode):
        task = app.ot_soup.element_by_path(n.path)
        assert isinstance(task, Task)

        # simplicity: show task metadata in a bullet list that contain
        # all that's necessary but is not overly beautiful.

        # TODO: find out how to create tables

        bl = nodes.bullet_list()

        # title
        elems = [nodes.Text(f'Title: {task.title}')]
        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        # path
        elems = [nodes.Text(f'Path: {".".join(task.path)}')]
        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        # ref
        elems = [nodes.Text('Ref: ')]
        ref = nodes.reference()
        ref['refuri'] = app.builder.get_relative_uri(
            from_=docname, to=task.docname)
        ref += nodes.Text('.'.join(task.path))
        elems.append(ref)

        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        # implementation_points
        elems = [nodes.Text(f'Implementation Points: {task.implementation_points}')]
        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        # documentation_points
        elems = [nodes.Text(f'Documentation Points: {task.documentation_points}')]
        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        # integration_points
        elems = [nodes.Text(f'Integration Points: {task.integration_points}')]
        p = nodes.paragraph()
        p += elems
        li = nodes.list_item()
        li += p
        bl += li

        n.replace_self(bl)
 
class _TaskMetaNode(nodes.Element):
    def __init__(self, path):
        super().__init__(self)
        self.path = path

class _TaskMetaDirective(SphinxDirective):
    required_arguments = 1   # path

    def run(self):
        path = utils.element_path(self.arguments[0].strip())

        l = _TaskMetaNode(path=path)
        l.document = self.state.document
        set_source_info(self, l)

        return [l]

