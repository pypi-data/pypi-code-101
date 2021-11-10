import os
import json

from nn_trainer.trainers.abstract_nn_trainer import AbstractNnTrainer

from nn_trainer.metrics import *
from nn_trainer.callbacks import *

import torch
import torch.nn
import torch.optim
import torch.utils.data as td

from typing import Dict

class BasicNnTrainer(AbstractNnTrainer):
    def __init__(
        self,
        args,
        neural_network: torch.nn.Module, 
        verbose: bool = False,
        patience: int = 0,
        optimizer_fn: Any = torch.optim.Adam,
        optimizer_params: Dict = dict(lr=2e-2),# field(default_factory=lambda: ),
        scheduler_fn: Any = None,
        scheduler_params: Dict = field(default_factory=dict),
        dtype: Any = torch.float32,
        logger: Any = None        
        ):
        super().__init__(
            args,
            neural_network,
            optimizer_fn,
            optimizer_params,
            scheduler_fn,
            scheduler_params,
            dtype,
            verbose,
            patience,
            logger
        )

    def train(
        self,
        training_data_set: td.Dataset,
        validation_data_set: td.Dataset, 
        callbacks: List[Callback] = [], 
        loss_fn = torch.nn.MSELoss(),
        metrics: List[Metric] = [],
        ):

        self._set_metrics(metrics, ['validation'])
        self._set_callbacks(callbacks)
        self._loss_fn = loss_fn
        
        self._dataset_train = training_data_set
        self._dataset_valid = validation_data_set
        self._train_data_loader = td.DataLoader(dataset=self._dataset_train, batch_size=self._batch_size, shuffle=True)
        self._valid_data_loader = td.DataLoader(dataset=self._dataset_valid, batch_size=self._batch_size, shuffle=True)
        
        self._eval_names = ['validation']

        with open(os.path.join(self._model_directory_path, 'training_config.json'), 'w') as f: json.dump(self._args, f, indent=4)

        self._stop_training = False

        # Call method on_train_begin for all callbacks
        self._callback_container.on_train_begin()
        
        for epoch_index in range(self._epoch_count):
            self._callback_container.on_epoch_begin(epoch_index)
            self._net_g.train()
            
            # train on batches here
            for batch_index, (i_real, o_real) in enumerate(self._train_data_loader):
                self._callback_container.on_batch_begin(batch_index)

                batch_logs = {"batch_size": i_real.shape[0]}

                i_real = self.to_tensor(i_real, self._dtype)
                o_real = self.to_tensor(o_real, self._dtype)
                
                for param in self._net_g.parameters():
                    param.grad = None

                o_fake = self._net_g(i_real)

                loss = self._loss_fn(o_real, o_fake)

                # Perform backward pass and optimization    
                loss.backward()
                torch.nn.utils.clip_grad_norm_(self._net_g.parameters(), 1)
                self._net_g_optimizer.step()

                batch_logs["loss"] = self.to_numpy(loss).item()
                
                self._callback_container.on_batch_end(batch_index, batch_logs)
            
            epoch_logs = {"lr": self._net_g_optimizer.param_groups[-1]["lr"]}
            self.history.epoch_metrics.update(epoch_logs)

            # Apply predict epoch to all validation set
            for eval_name, valid_data in zip(self._eval_names, self._valid_data_loader):
                self._predict_epoch(eval_name, valid_data)

            # Call method on_epoch_end for all callbacks
            self._callback_container.on_epoch_end(epoch_index, logs=self.history.epoch_metrics)

            if self._stop_training:
                break
        
        # Call method on_train_end for all callbacks
        self._callback_container.on_train_end()
        self.network.eval()
       
    def _set_callbacks(self, custom_callbacks):
        """Setup the callbacks functions.
        Parameters
        ----------
        custom_callbacks : list of func
            List of callback functions.
        """
        # Setup default callbacks history, early stopping and scheduler
        callbacks = []
        self.history = History(self, verbose=self._verbose, logger=self._logger)
        callbacks.append(self.history)
        if (self.early_stopping_metric is not None) and (self._patience > 0):
            early_stopping = EarlyStopping(early_stopping_metric=self.early_stopping_metric, is_maximize=(self._metrics[-1]._maximize if len(self._metrics) > 0 else None), patience=self._patience, logger=self._logger)
            callbacks.append(early_stopping)
        else:
            print("No early stopping will be performed, last training weights will be used.")
        if self._net_g_scheduler_fn is not None:
            # Add LR Scheduler call_back
            is_batch_level = self._net_g_scheduler_params.pop("is_batch_level", False)
            scheduler = LRSchedulerCallback(scheduler_fn=self._net_g_scheduler_fn, scheduler_params=self._net_g_scheduler_params, optimizer=self._net_g_optimizer, early_stopping_metric=self.early_stopping_metric, is_batch_level=is_batch_level)
            callbacks.append(scheduler)

        if custom_callbacks:
            callbacks.extend(custom_callbacks)
        self._callback_container = CallbackContainer(callbacks)
        self._callback_container.set_trainer(self)