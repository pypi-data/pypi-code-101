from . import utils
from . import soup
from ..grading import Grading
from ..errors import OpenTrainingError

from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import set_source_info
from docutils import nodes


from sphinx.util import logging
_logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive('ot-pointscollected', _PointsCollectedDirective)
    app.connect('doctree-resolved', _ev_doctree_resolved__expand_pointscollected_nodes)

def _ev_doctree_resolved__expand_pointscollected_nodes(app, doctree, docname):
    for n in doctree.traverse(_PointsCollectedNode):
        persons = []
        tasks = []
        for person in n.persons:
            try:
                persons.append(app.ot_soup.element_by_path(person, userdata=n))
            except OpenTrainingError as e:
                _logger.warning(e, location=n)
        for task in n.tasks:
            try:
                tasks.append(app.ot_soup.element_by_path(task, userdata=n))
            except OpenTrainingError as e:
                _logger.warning(e, location=n)

        grading = Grading(persons = persons, tasks = tasks)
        bl = nodes.bullet_list()
        for person, points in grading.points_per_person():
            elems = [nodes.Text(f'{person.title}: {points}')]
            p = nodes.paragraph()
            p += elems
            li = nodes.list_item()
            li += p
            bl += li
            
        n.replace_self([bl])

class _PointsCollectedNode(nodes.Element):
    def __init__(self, persons, tasks):
        super().__init__(self)
        self.title = None
        self.persons = persons
        self.tasks = tasks

class _PointsCollectedDirective(SphinxDirective):
    required_arguments = 0

    option_spec = {
        'persons': utils.list_of_elementpath,
        'tasks': utils.list_of_elementpath,
    }

    def run(self):
        persons = self.options.get('persons')
        tasks = self.options.get('tasks')

        pointcollected = _PointsCollectedNode(
            persons = persons,
            tasks = tasks,
        )

        pointcollected.document = self.state.document
        set_source_info(self, pointcollected)

        return [pointcollected]
