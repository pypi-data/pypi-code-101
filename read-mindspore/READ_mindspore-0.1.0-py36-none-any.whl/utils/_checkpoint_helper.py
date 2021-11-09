import logging
from mindspore import Tensor, export
from mindspore import save_checkpoint
from collections import Counter, OrderedDict
import numpy as np

class EarlyStop():
    """Used to early stop the training if validation loss doesn't improve after a given patience."""
    def __init__(self, patience=20, verbose=True, delta=0, save_name="checkpoint"):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 20
            verbose (bool): If True, prints a message for each validation loss improvement.
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
            save_name (string): The filename with which the model and the optimizer is saved when improved.
                            Default: "checkpoint.pt"
        """
        self.patience = patience
        self.verbose = verbose
        self.save_name = save_name
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.logger = logging.getLogger('READ.Train')

    def __call__(self, val_loss, model, imsize):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model, imsize)
        elif score < self.best_score - self.delta:
            self.counter += 1
            self.logger.info(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model, imsize)
            self.counter = 0

        return self.early_stop

    def save_checkpoint(self, val_loss, model, imsize):
        '''Saves model when validation loss decrease.'''
        if self.verbose:
            self.logger.info(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        # inputs = Tensor(np.ones([1, 3, imsize[0], imsize[1]]).astype(np.float32))
        # export(model, inputs, file_name=self.save_name, file_format='MINDIR')
        save_checkpoint(model, self.save_name)
        self.val_loss_min = val_loss

def remove_dataparallel(state_dict):
    """Remover data parallel when loading state dict
    Args:
        state_dict: saved state dict with data parallel

    Returns:
        new state dict without `module`
    Raises:
        IOError: An error occurred accessing state_dice object.
    """
    new_state_dict = OrderedDict()
    for k,v in state_dict.items():
        if k[:7] == "module.": #remove module.
            name = k[7:]
        else:
            name = k
        new_state_dict[name] = v

    return new_state_dict
