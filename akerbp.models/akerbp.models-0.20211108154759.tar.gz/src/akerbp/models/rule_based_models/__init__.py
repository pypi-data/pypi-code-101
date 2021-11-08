import os
import joblib
import pandas as pd
import importlib

from mlpet.Datasets import lithology
from akerbp.models import Model
from akerbp.models import classification_models
from akerbp.models.rule_based_models import helpers

class BadlogModel(Model):
    def __init__(self, **kwargs):
        """
        Initializes badlog model
        """
        self.kwargs = kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)
        
    def predict(self, X, methods, **kwargs):
        """
        Args:
            X (dict or pd.DataFrame): expected features

        Returns:
            y (pd.DataFrame): including different badlog flags
        """
        if isinstance(X, dict):
            if 'metadata' not in X.keys():
                raise ValueError('"metadata" key is required')
            if 'data' not in X.keys():
                raise ValueError('"data" key is required')
            X_df = pd.DataFrame.from_dict(X['data'])
            metadata = X['metadata']
            self.X_pred, num_cols, cat_cols = helpers._apply_metadata(X_df, **kwargs.get('_metadata', metadata))
        elif isinstance(X, pd.core.frame.DataFrame):
            X_df = X
            self.X_pred, num_cols, cat_cols = helpers._apply_metadata(X_df, **kwargs.get('_metadata', {}))
        else:
            raise ValueError('Please pass the data as a dict or a pandas DataFrame')
        
        #Validate feature
        self.X_pred = helpers._create_features(self.X_pred)

        self.X_pred_features = set(list(self.X_pred.columns))
        self.expected_curves = set(['DEPTH', 'DEN', 'DENC', 'AC', 'ACS', 'BS', 'CALI', 'GR', 'NEU', 'RDEP', 'RMED', 'RMIC', 'PEF', 'GROUP'])
        helpers._validate_features(self.X_pred_features, self.expected_curves)

        self.methods = methods
        self.y = pd.DataFrame()

        for method in self.methods:
            #Evaluate method
            method_helpers = importlib.import_module('ml_petrophysics.models.rule_based_models.{}_helpers'.format(method))
            method_evaluator = getattr(method_helpers, 'flag_{}'.format(method))
            if method == 'crossplot':

                cp_names = kwargs.get('cp_names', ['vp_den', 'vp_vs', 'ai_vpvs'])
                #Make sure both dataset- and model- settings are provided
                settings = kwargs.get('settings', None)
                mappings = kwargs.get('mappings', None)
                folder_path = kwargs.get('folder_path', None)
                #Assuming all cp_names use the same model- and data-settings
                model_settings = settings['models']
                data_settings = settings['datasets']['lithology']

                #Instantiate datasets and models for each of the crossplots
                datasets = dict()
                models = dict()
                key_wells = dict()
                folder_paths = dict()

                for cp_name in cp_names:
                    print('init ds and model - BadlogModel - {}'.format(cp_name))
                    folder_paths[cp_name] = os.path.join(folder_path, cp_name)
                    datasets[cp_name] = lithology.Lithologydata(
                        settings=data_settings, 
                        mappings=mappings,
                        folder_path=folder_paths[cp_name]
                        ) #but don't load any data into the dataset, because we need to get that from running the find_crossplot_scores
                    
                    models[cp_name] = classification_models.XGBoostClassificationModel(
                        model_settings, 
                        folder_paths[cp_name]
                        )

                    key_wells[cp_name] = joblib.load(os.path.join(folder_paths[cp_name], 'key_wells.joblib'))

                method_flags = method_evaluator(self.X_pred, cp_names, datasets, models, key_wells)
            else:
                method_flags = method_evaluator(self.X_pred)
            self.y[method_flags.columns] = method_flags
        result_columns = [col for col in self.y.columns.tolist() if col not in self.X_pred.columns.tolist()]
        return self.y[result_columns]

