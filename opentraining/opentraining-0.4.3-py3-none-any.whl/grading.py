from collections import defaultdict


class Grading:
    def __init__(self, persons, tasks):
        self.persons = persons
        self.tasks = tasks

    def points_per_person(self):
        'Return iterable of (person, points)'

        points_per_person = defaultdict(int)

        for task in self.tasks:
            for person, share in task.implementors:
                points = share * task.implementation_points
                points_per_person[person] += points
            for person, share in task.documenters:
                points = share * task.documentation_points
                points_per_person[person] += points
            for person, share in task.integrators:
                points = share * task.integration_points
                points_per_person[person] += points

        return ((person, points_per_person[person]) for person in self.persons)
