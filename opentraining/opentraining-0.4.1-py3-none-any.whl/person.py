from .node import Node


class Person(Node):  # is-a Node only because that holds path,
                     # docname, and userdata
    def __init__(self, title, path, docname, userdata, firstname,
                 lastname):
        super().__init__(
            title=title, 
            path=path, 
            docname=docname, 
            userdata=userdata,
            dependencies=[], 
            )
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'Person:{str(super())}, firstname:{self.firstname}, lastname:{self.lastname}'
