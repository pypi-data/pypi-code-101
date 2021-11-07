from .i_experiment import IExperiment


class Explainer:

    def __init__(self, exp: IExperiment):
        self.exp = exp

    def explain(self):
        pass
