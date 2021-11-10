import os
import json

import numpy
from nn_trainer.trainers.abstract_nn_trainer import AbstractNnTrainer


from nn_trainer.metrics import *
from nn_trainer.callbacks import *
from nn_trainer.trainers import *

import torch
import torch.nn
import torch.optim
import torch.utils.data as td

from typing import Dict

class VanillaGanNnTrainer(AbstractNnTrainer):
    def __init__(
        self,
        args,
        generator_neural_network: torch.nn.Module, 
        discriminator_neural_network: torch.nn.Module, 
        generator_optimizer_fn: Any = torch.optim.Adam,
        generator_optimizer_params: Dict = dict(lr=0.0002),
        discriminator_optimizer_fn: Any = torch.optim.Adam,
        discriminator_optimizer_params: Dict = dict(lr=0.0002),
        scheduler_fn: Any = None,
        scheduler_params: Dict = field(default_factory=dict),
        dtype: Any = torch.float32,
        verbose: bool = False,
        patience: int = 0,
        logger: Any = None,
        ):
        super().__init__(
            args,
            generator_neural_network, 
            generator_optimizer_fn,
            generator_optimizer_params,
            scheduler_fn,
            scheduler_params,
            dtype,
            verbose,
            patience,
            logger)
        self._net_d = discriminator_neural_network.type(dtype)
        self._net_d.to(self._device)
        self._net_d_optimizer_fn = discriminator_optimizer_fn
        self._net_d_optimizer_params = discriminator_optimizer_params
        self._net_d_scheduler_fn = scheduler_fn
        self._net_d_scheduler_params = scheduler_params

        self._net_d_optimizer = self._net_d_optimizer_fn(self._net_d.parameters(), **self._net_d_optimizer_params)

        self._discriminator_model_directory_path = make_path(os.path.join(self._model_directory_path, self._net_d.__class__.__name__))

    def train(
        self,
        training_data_set: td.Dataset,
        validation_data_set: td.Dataset, 
        callbacks: List[Callback] = [], 
        loss_fn = torch.nn.BCELoss(),
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
            self._net_d.train()
            
            # train on batches here
            for batch_index, (i_real, o_real) in enumerate(self._train_data_loader):
                self._callback_container.on_batch_begin(batch_index)

                batch_logs = {"batch_size": i_real.shape[0]}

                i_real = self.to_tensor(i_real, self._dtype)
                o_real = self.to_tensor(o_real, self._dtype)

                real = self.to_tensor(numpy.ones(shape=(o_real.shape[0], 1)), self._dtype)
                fake = self.to_tensor(numpy.zeros(shape=(o_real.shape[0], 1)), self._dtype)
                
                ######################
                ## Train generator
                ######################

                # zero_grad here
                self._net_g_optimizer.zero_grad()
                #for param in self._net_g.parameters(): param.grad = None

                o_fake = self._net_g(i_real)
                d_result = self._net_d(i_real, o_fake)

                g_loss = self._loss_fn(d_result, real)

                # Perform backward pass and optimization    
                g_loss.backward()
                torch.nn.utils.clip_grad_norm_(self._net_g.parameters(), 1)
                self._net_g_optimizer.step()

                batch_logs["g_loss"] = self.to_numpy(g_loss).item()
                
                ######################
                ## Train discriminator
                ######################

                # zero_grad here
                self._net_d_optimizer.zero_grad()
                #for param in self._net_d.parameters(): param.grad = None

                # Measure discriminator's ability to classify real from generated samples
                real_loss = self._loss_fn(self._net_d(i_real, o_real), real)
                fake_loss = self._loss_fn(self._net_d(i_real, o_fake.detach()), fake)
                d_loss = (real_loss + fake_loss) / 2

                d_loss.backward()
                self._net_d_optimizer.step()

                batch_logs["loss"] = self.to_numpy(d_loss).item()
                batch_logs["d_loss"] = self.to_numpy(d_loss).item()

                self._callback_container.on_batch_end(batch_index, batch_logs)
            
            epoch_logs = { 
                "lr_net_g": self._net_g_optimizer.param_groups[-1]["lr"],
                "lr_net_d": self._net_d_optimizer.param_groups[-1]["lr"] 
                }
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
        self._net_g.eval()
        self._net_d.eval()
       
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
            if self._logger is not None:
                self._logger.info("No early stopping will be performed, last training weights will be used.")
        if self._net_g_scheduler_fn is not None:
            # Add LR Scheduler call_back for generator
            is_batch_level = self._net_g_scheduler_params.pop("is_batch_level", False)
            net_g_scheduler = LRSchedulerCallback(scheduler_fn=self._net_g_scheduler_fn, scheduler_params=self._net_g_scheduler_params, optimizer=self._net_g_optimizer, early_stopping_metric=self.early_stopping_metric, is_batch_level=is_batch_level)
            callbacks.append(net_g_scheduler)
        if self._net_d_scheduler_fn is not None:
            # Add LR Scheduler call_back for discriminator
            is_batch_level = self._net_d_scheduler_params.pop("is_batch_level", False)
            net_d_scheduler = LRSchedulerCallback(scheduler_fn=self._net_d_scheduler_fn, scheduler_params=self._net_d_scheduler_params, optimizer=self._net_d_optimizer, early_stopping_metric=self.early_stopping_metric, is_batch_level=is_batch_level)
            callbacks.append(net_d_scheduler)

        if custom_callbacks:
            callbacks.extend(custom_callbacks)
        self._callback_container = CallbackContainer(callbacks)
        self._callback_container.set_trainer(self)