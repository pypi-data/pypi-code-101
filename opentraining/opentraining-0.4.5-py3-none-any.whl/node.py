from .element import Element


class Node(Element):
    def __init__(self, title, path, docname, dependencies, userdata):
        super().__init__(
            title=title, 
            path=path, 
            docname=docname, 
            userdata=userdata)
        self.dependencies = dependencies
