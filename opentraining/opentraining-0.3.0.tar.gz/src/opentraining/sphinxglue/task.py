from . import utils
from . import soup
from .. import errors
from ..task import Task

from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import set_source_info
from sphinx.util import logging
from docutils import nodes

logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive('ot-task', _TaskDirective)
    app.connect('doctree-read', _ev_doctree_read__extract_tasknodes)

def _ev_doctree_read__extract_tasknodes(app, doctree):
    try:
        docname = app.env.docname
        task_nodes = list(doctree.traverse(_TaskNode))
        if len(task_nodes) > 1:
            raise errors.OpenTrainingError(f'{docname} contains multiple tasks')

        for n in task_nodes:
            soup.sphinx_add_element(app, Task(
                title = utils.get_document_title(docname, doctree),
                docname = docname,
                path = n.path, 
                dependencies = n.dependencies,
                userdata = n,

                implementation_points = n.implementation_points,
                documentation_points = n.documentation_points,
                integration_points = n.integration_points,
                implementors = n.implementors,
                documenters = n.documenters,
                integrators = n.integrators,
            ))
            n.replace_self([])
    except Exception:
        logger.exception(f'{docname}: cannot extract task nodes')
        raise
        
class _TaskNode(nodes.Element):
    def __init__(self, path, dependencies,
                 implementation_points, documentation_points, integration_points,
                 implementors, documenters, integrators,
                 responsible, initial_estimate, spent, percent_done):
        super().__init__(self)
        self.title = None
        self.path = path

        self.implementation_points = implementation_points
        self.documentation_points = documentation_points
        self.integration_points = integration_points
        self.implementors = implementors
        self.documenters = documenters
        self.integrators = integrators

        self.dependencies = dependencies
        self.responsible = responsible
        self.initial_estimate = initial_estimate
        self.spent = spent
        self.percent_done = percent_done

class _TaskDirective(SphinxDirective):
    required_arguments = 1   # path

    option_spec = {
        'implementation-points': int,
        'documentation-points': int,
        'integration-points': int,
        'implementors': utils.list_of_person_and_share,
        'documenters': utils.list_of_person_and_share,
        'integrators': utils.list_of_person_and_share,
        'dependencies': utils.list_of_elementpath,
        'responsible': str,
        'initial-estimate': int,
        'spent': int,
        'percent-done': int,
    }

    def run(self):
        path = utils.element_path(self.arguments[0].strip())
        dependencies = self.options.get('dependencies', [])

        implementation_points = self.options.get('implementation-points')
        documentation_points = self.options.get('documentation-points')
        integration_points = self.options.get('integration-points')
        implementors = self.options.get('implementors', [])
        documenters = self.options.get('documenters', [])
        integrators = self.options.get('integrators', [])

        responsible = self.options.get('responsible', '')
        initial_estimate = self.options.get('initial-estimate', 0)
        spent = self.options.get('spent', 0)
        percent_done = self.options.get('percent-done', 0)

        task = _TaskNode(path = path, 

                         implementation_points = implementation_points,
                         documentation_points = documentation_points,
                         integration_points = integration_points,
                         implementors = implementors,
                         integrators = integrators,
                         documenters = documenters,

                         dependencies = dependencies,
                         responsible = responsible,
                         initial_estimate = initial_estimate, 
                         spent = spent, 
                         percent_done = percent_done)
        task.document = self.state.document
        set_source_info(self, task)

        return [task]
