from torch.optim import lr_scheduler
from scipy.stats import logistic
import numpy as np


class CustomScheduler(lr_scheduler._LRScheduler):

    def __init__(self, optimizer):
        self.n_params = len(optimizer.param_groups)
        super().__init__(optimizer)

    @property
    def lrs(self):
        return self._lrs  # implement me!

    def get_lr(self):
        for i in range(self.n_params):
            if self.last_epoch < self._lrs.shape[0]:
                self.lr_history.append(self._lrs[self.last_epoch])
                yield self._lrs[self.last_epoch]
                
            else:
                self.lr_history.append(self._lrs[self._lrs.shape[0]-1])
                yield self._lrs[self._lrs.shape[0]-1]


class WarmupRolloffScheduler(CustomScheduler):

    def __init__(self, optimizer, start_lr, peak_lr, peak_epoch, final_lr, final_epoch):
        self._lrs = self.get_lrs(start_lr, peak_lr, peak_epoch, final_lr, final_epoch)
        super().__init__(optimizer)

    def get_lrs(self, start_lr, peak_lr, peak_epoch, final_lr, final_epoch):
        # warmup from start to peak
        lrs = np.zeros((final_epoch,))
        lrs[0:peak_epoch] = np.linspace(start_lr, peak_lr, peak_epoch)

        # setup rolloff params
        length = final_epoch - peak_epoch
        magnitude = peak_lr - final_lr

        # rolloff to final
        rolloff_lrs = self.rolloff(length, magnitude=magnitude, offset=final_lr)
        lrs[peak_epoch:] = rolloff_lrs
        return lrs

    def rolloff(self, length, loc_factor=0.5, scale_factor=0.1, magnitude=1, offset=0):
        """
        Produces a rolloff function over a given length. Imagine 1 - sigmoid(x).
        """
        loc = length * loc_factor
        scale = length * scale_factor
        rolloff = np.array([logistic.sf(x, loc, scale) for x in range(length)])
        rolloff *= magnitude
        rolloff += offset
        return rolloff

class CosineAnnealingScheduler(lr_scheduler._LRScheduler):

    def __init__(self, optimizer, start_anneal, n_epochs):
        self.curve = self.get_curve(1, start_anneal, n_epochs)
        self.initial_lrs = [param_group['lr'] for param_group in optimizer.param_groups]
        self.lr_history = []
        super().__init__(optimizer)

    def rolloff(self, length, loc_factor=0.5, scale_factor=0.1, magnitude=1, offset=0):
        """
        Produces a rolloff function over a given length. Imagine 1 - sigmoid(x).
        """
        loc = length * loc_factor
        scale = length * scale_factor
        rolloff = np.array([logistic.sf(x, loc, scale) for x in range(length)])
        rolloff *= magnitude
        rolloff += offset
        return rolloff

    def get_curve(self, start_lr, start_anneal, n_epochs):
        # constant LR to start
        lrs = np.zeros((n_epochs,))
        lrs[0:start_anneal] = start_lr

        # setup rolloff params
        length = n_epochs - start_anneal

        # rolloff to zero
        rolloff_lrs = self.rolloff(length, loc_factor=0.5, scale_factor=0.1, magnitude=start_lr)
        lrs[start_anneal:] = rolloff_lrs
        return lrs

    def get_lr(self):
        for i, init_lr in enumerate(self.initial_lrs):
            if self._step_count - 1 < self.curve.shape[0]:
                lr = init_lr * self.curve[self._step_count - 1]
                self.lr_history.append(lr)
                yield lr
            else:
                lr = init_lr * self.curve[self._step_count - 2]
                self.lr_history.append(lr)
                yield lr


# -- Util functions --


def sin_decay(offset, amplitude, n_periods, n_epochs, gamma):
    """
    Produces a sinusoidal decay function.
    """
    max_x = n_periods * 2 * np.pi
    xs = np.linspace(0, max_x, n_epochs)
    sin = np.sin(xs)
    gammas = np.array([gamma ** x for x in range(n_epochs)])
    sin *= gammas
    sin -= (1 - gammas)
    sin += 1
    sin *= amplitude / 2
    sin += offset
    return sin


class CosineAnnealingLR_with_Restart(lr_scheduler._LRScheduler):
    """Set the learning rate of each parameter group using a cosine annealing
    schedule, where :math:`\eta_{max}` is set to the initial lr and
    :math:`T_{cur}` is the number of epochs since the last restart in SGDR:
    .. math::
        \eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})(1 +
        \cos(\frac{T_{cur}}{T_{max}}\pi))
    When last_epoch=-1, sets initial lr as lr.
    It has been proposed in
    `SGDR: Stochastic Gradient Descent with Warm Restarts`_. The original pytorch
    implementation only implements the cosine annealing part of SGDR,
    I added my own implementation of the restarts part.
    Args:
        optimizer (Optimizer): Wrapped optimizer.
        T_max (int): Maximum number of iterations.
        T_mult (float): Increase T_max by a factor of T_mult
        eta_min (float): Minimum learning rate. Default: 0.
        last_epoch (int): The index of last epoch. Default: -1.
        model (pytorch model): The model to save.
        out_dir (str): Directory to save snapshots
        take_snapshot (bool): Whether to save snapshots at every restart
    .. _SGDR\: Stochastic Gradient Descent with Warm Restarts:
        https://arxiv.org/abs/1608.03983
    """

    def __init__(self, optimizer, T_max, T_mult, model, out_dir, take_snapshot, eta_min=0, last_epoch=-1):
        self.T_max = T_max
        self.T_mult = T_mult
        self.Te = self.T_max
        self.eta_min = eta_min
        self.current_epoch = last_epoch

        self.model = model
        self.out_dir = out_dir
        self.take_snapshot = take_snapshot

        self.lr_history = []

        super(CosineAnnealingLR_with_Restart, self).__init__(optimizer, last_epoch)

    def get_lr(self):
        new_lrs = [self.eta_min + (base_lr - self.eta_min) *
                   (1 + math.cos(math.pi * self.current_epoch / self.Te)) / 2
                   for base_lr in self.base_lrs]

        self.lr_history.append(new_lrs)
        return new_lrs

    def step(self, epoch=None):
        if epoch is None:
            epoch = self.last_epoch + 1
        self.last_epoch = epoch
        self.current_epoch += 1

        for param_group, lr in zip(self.optimizer.param_groups, self.get_lr()):
            param_group['lr'] = lr

        ## restart
        if self.current_epoch == self.Te:
            print("restart at epoch {:03d}".format(self.last_epoch + 1))

            if self.take_snapshot:
                torch.save({
                    'epoch': self.T_max,
                    'state_dict': self.model.state_dict()
                }, self.out_dir + "Weight/" + 'snapshot_e_{:03d}.pth.tar'.format(self.T_max))

            ## reset epochs since the last reset
            self.current_epoch = 0

            ## reset the next goal
            self.Te = int(self.Te * self.T_mult)
            self.T_max = self.T_max + self.Te

            return True
        else:
            return False