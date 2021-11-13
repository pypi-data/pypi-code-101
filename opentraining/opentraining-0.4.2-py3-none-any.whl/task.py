from .node import Node


class Task(Node):
    def __init__(self, 
                 title, path, docname, 
                 dependencies, userdata,

                 implementation_points, implementors,
                 documentation_points, documenters,
                 integration_points, integrators):

        if len(implementors) != 0:
            assert sum(share for person, share in implementors) == 100
        if len(documenters) != 0:
            assert sum(share for person, share in documenters) == 100
        if len(integrators) != 0:
            assert sum(share for person, share in integrators) == 100

        super().__init__(
            title=title, 
            path=path, 
            docname=docname, 
            # add persons as task dependencies
            dependencies=dependencies + [person for person, share in implementors + documenters + integrators], 
            userdata=userdata)

        self.implementation_points = implementation_points
        self.documentation_points = documentation_points
        self.integration_points = integration_points

        self.implementors = implementors
        self.documenters = documenters
        self.integrators = integrators

    def __str__(self):
        return 'Task:'+super().__str__()

    def resolve_paths(self, soup):
        resolved_implementors = []
        for person_path, share in self.implementors:
            person = soup.element_by_path(person_path)
            resolved_implementors.append((person, share))
        resolved_documenters = []
        for person_path, share in self.documenters:
            person = soup.element_by_path(person_path)
            resolved_documenters.append((person, share))
        resolved_integrators = []
        for person_path, share in self.integrators:
            person = soup.element_by_path(person_path)
            resolved_integrators.append((person, share))

        self.implementors = resolved_implementors
        self.documenters = resolved_documenters
        self.integrators = resolved_integrators
