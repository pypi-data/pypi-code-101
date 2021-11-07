from ..model.classifier import IClassifier
from .utils import Dataset

class IExperiment:
    clf: IClassifier # vraiment bien de mettre la parent class here ?
    train: Dataset
    valid: Dataset
    test: Dataset
    target: str
    num_features: list
    cat_features: list
    #text_features: list = None, # not supported for the moment
    thresholds: dict
    precision_target: float
    random_seed: int
    labels: list
    verbose: int
    fillna_value_cat: str
    fillna_value_num: float
    below_threshold_label: str

    def make(self):
        pass

    def save(self, filename):
        pass

    def load(self, filename):
        pass

    def generate_report(self):
        "idea is to generate of report with all interesting things automatically"
        pass
