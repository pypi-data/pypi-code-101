from abc import abstractmethod
import io
import os
import os.path

import json
from pathlib import Path
import shutil
import zipfile
import warnings
import copy
import numpy
from numpy import ndarray
from nn_trainer.models.networks.networks_1d import init_weights

import datetime

from nn_trainer.metrics import *
from nn_trainer.callbacks import *

import torch
import torch.nn
import torch.optim
import torch.utils.data as td
import torch.nn.functional as f

from typing import Dict

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int64):
            return int(obj)
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, torch.Tensor):
            return obj.cpu().numpy()
        elif isinstance(obj, torch.dtype):
            return str(obj)

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def make_path(output_path):
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    return output_path

class AbstractNnTrainer(object):
    def __init__(
        self,
        args,
        neural_network: torch.nn.Module, 
        optimizer_fn: Any = torch.optim.Adam,
        optimizer_params: Dict = dict(lr=2e-2),
        scheduler_fn: Any = None,
        scheduler_params: Dict = field(default_factory=dict),
        dtype: Any = torch.float32,
        verbose: bool = False,
        patience: int = 0,
        logger = None
        ):
        self._args = args
        self._verbose = verbose
        self._patience = patience
        self._logger = logger
        
        self._is_cuda_enabled = True if torch.cuda.is_available() else False
        self._device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self._ngpus = torch.cuda.device_count() if torch.cuda.is_available() else 0
        self._dtype = dtype

        self._net_g = neural_network.type(dtype)
        self._net_g.to(self._device)
        self._net_g_optimizer_fn = optimizer_fn
        self._net_g_optimizer_params = optimizer_params
        self._net_g_scheduler_fn = scheduler_fn
        self._net_g_scheduler_params = scheduler_params

        self._net_g_optimizer = self._net_g_optimizer_fn(self._net_g.parameters(), **self._net_g_optimizer_params)

        self._epoch_count = args['max_epoch_count']
        self._batch_size = args['batch_size']
        self._model_directory_path = make_path(os.path.join(args['output_dir'], "{}_{}".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"), self.__class__.__name__))) 
        self._generator_model_directory_path = make_path(os.path.join(self._model_directory_path, self._net_g.__class__.__name__))

    @property
    def device(self):
        return self._device

    @property
    def network(self):
        return self._net_g

    @property
    def network_dtype(self):
        return self._dtype

    @property
    def output_directory_path(self):
        return self._model_directory_path
    
    def to_tensor(self, data, dtype=torch.float32):
        if isinstance(data, list):
            result = torch.tensor(numpy.asarray(data), dtype=dtype).to(device=self._device)
        elif isinstance(data, ndarray):
            result = torch.tensor(data, dtype=dtype).to(device=self._device)
        elif isinstance(data, torch.Tensor):
            result = data.clone().detach().requires_grad_(data.requires_grad).to(device=self._device, dtype=self._dtype)
        else:
            raise TypeError("type {} of data is not acceptable".format(type(data)))
        return result

    def to_numpy(self, data: torch.Tensor):
        if data.requires_grad:
            data = data.detach()
        if self._device == torch.device("cuda:0"):
            data = data.cpu()
        return data.numpy()

    @abstractmethod
    def train(
        self,
        training_data_set: td.Dataset,
        validation_data_set: td.Dataset, 
        callbacks: List[Callback] = [], 
        loss_fn = torch.nn.MSELoss(),
        metrics: List[Metric] = [],
        ):
        raise NotImplementedError("train method must be implemented")

    def save_model(self, model_name):
        """Saving the model.  This method reuses the model output directory property 
        initialized during construction of this object.
        Parameters
        ----------
        model_name : str
            The name to give to the model. Recommendation: use epoch in the name
        Returns
        -------
        str
            input filepath with ".pt" appended
        """
        path = self.output_directory_path + "\\{}".format(model_name)

        saved_params = {}
        init_params = {}
        for key, val in self._net_g.state_dict().items():
            if isinstance(val, type):
                # Don't save torch specific params
                continue
            else:
                init_params[key] = { 'shape': val.shape, 'dtype': val.dtype }
        init_params["device_type"] = self._device.type
        init_params["device_index"] = self._device.index
        saved_params["init_params"] = init_params

        # Create folder
        Path(path).mkdir(parents=True, exist_ok=True)
        
        # Save models params
        with open(Path(path).joinpath("model_params.json"), "w", encoding="utf8") as f:
            json.dump(saved_params, f, cls=ComplexEncoder, indent=4)

        # Save state_dict
        torch.save(self.network.state_dict(), Path(path).joinpath("network.pt"))
        shutil.make_archive(path, "zip", path)
        shutil.rmtree(path)
        print(f"Successfully saved model at {path}.zip")
        return f"{path}.zip"

    def load_model(self, filepath):
        """Load TabNet model.
        Parameters
        ----------
        filepath : str
            Path of the model.
        """
        path = Path(filepath)
        if path.suffix == "":
            path = Path(filepath + ".zip")
        
        if path.suffix != ".zip":
            raise TypeError("non zip files are not supported")

        try:
            with zipfile.ZipFile(path) as z:
                with z.open("model_params.json") as f:
                    loaded_params = json.load(f)
                    loaded_params["init_params"]["device_name"] = self._device
                with z.open("network.pt") as f:
                    try:
                        saved_state_dict = torch.load(f, map_location=self.device)
                    except io.UnsupportedOperation:
                        # In Python <3.7, the returned file object is not seekable (which at least
                        # some versions of PyTorch require) - so we'll try buffering it in to a
                        # BytesIO instead:
                        saved_state_dict = torch.load(io.BytesIO(f.read()), map_location=self.device)
        except KeyError:
            raise KeyError("Your zip file is missing at least one component")

        #self.__init__(**loaded_params["init_params"])

        #self._set_network()
        self.network.load_state_dict(saved_state_dict)
        self.network.eval()
        #self.load_class_attrs(loaded_params["class_attrs"])

        return

    @abstractmethod
    def _set_callbacks(self, custom_callbacks):
        raise NotImplementedError("_set_callbacks method must be implemented")
    
    def _set_metrics(self, metrics, eval_names):
        """Set attributes relative to the metrics.
        Parameters
        ----------
        metrics : list of str
            List of eval metric names.
        eval_names : list of str
            List of eval set names.
        """
        metrics = metrics or [RMSE]

        metrics = check_metrics(metrics)
        # Set metric container for each sets
        self._metric_container_dict = {}
        for name in eval_names:
            self._metric_container_dict.update({name: MetricContainer(metrics, prefix=f"{name}_metric__")})

        self._metrics = []
        self._metrics_names = []
        for _, metric_container in self._metric_container_dict.items():
            self._metrics.extend(metric_container.metrics)
            self._metrics_names.extend(metric_container.names)

        # Early stopping metric is the last eval metric
        self.early_stopping_metric = (self._metrics_names[-1] if len(self._metrics_names) > 0 else None)

    def _predict_epoch(self, name, data):
        """
        Predict an epoch and update metrics.

        Parameters
        ----------
        name : str
            Name of the validation set
        loader : torch.utils.data.Dataloader
                DataLoader with validation set
        """
        # Setting network on evaluation mode
        self._net_g.eval()

        list_y_true = []
        list_y_score = []
        
        # Main loop
        X = data[0]
        y = data[1]
        scores = self._predict_batch(X)
        list_y_true.append(y)
        list_y_score.append(scores)

        y_true, scores = self._stack_batches(list_y_true, list_y_score)

        metrics_logs = self._metric_container_dict[name](y_true, scores)
        self._net_g.train()
        self.history.epoch_metrics.update(metrics_logs)
        return

    def _predict_batch(self, X):
        """
        Predict one batch of data.

        Parameters
        ----------
        X : torch.Tensor
            Owned products

        Returns
        -------
        np.array
            model scores
        """
        X = self.to_tensor(X)
        #X = X.to(self._device).float()

        # compute model output
        scores = self._net_g(X)

        if isinstance(scores, list):
            scores = [self.to_numpy(x) for x in scores]
        else:
            scores = self.to_numpy(scores)#cpu().detach().numpy()

        return scores
    
    def _stack_batches(self, list_y_true, list_y_score):
        y_true = np.vstack(list_y_true)
        y_score = np.vstack(list_y_score)
        return y_true, y_score