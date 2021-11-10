import os, time
import errno
import torch

class Logger(object):
    def __init__(self, model_name: str):
        return
    
    def log(self, d_error, g_error, epoch_index, batch_index):
         # var_class = torch.autograd.variable.Variable
        if isinstance(d_error, torch.autograd.Variable):            d_error = d_error.data.cpu().numpy()
        if isinstance(g_error, torch.autograd.Variable):            g_error = g_error.data.cpu().numpy()

        step = Logger._step(epoch_index, batch_index, self.num_batches)
        self.steps.append(step)
        self.d_losses.append(d_error)
        self.g_losses.append(g_error)

    def display_status(self, d_error, g_error, d_pred_real, d_pred_fake, epoch_index, batch_index):
        if isinstance(d_error, torch.autograd.Variable):
            d_error = d_error.data.cpu().numpy()
        if isinstance(g_error, torch.autograd.Variable):
            g_error = g_error.data.cpu().numpy()

        current_elapsed_time = time.time() - self.object_construction_time
        print('Elapsed Time: {:.4f} Epoch: [{}/{}], Batch Num: [{}/{}] Discriminator Loss: {:.4f}, Generator Loss: {:.4f} D(x,y): {:.4f}, D(G(z,y),y): {:.4f}'.format(current_elapsed_time, epoch_index, self.num_epochs, batch_index, self.num_batches, d_error, g_error, d_pred_real.mean(), d_pred_fake.mean()))
        print('     Discriminator Loss: {:.4f}, Generator Loss: {:.4f} D(x,y): {:.4f}, D(G(z,y),y): {:.4f}'.format(d_error, g_error, d_pred_real.mean(), d_pred_fake.mean()))
        print('     D(x,y): {:.4f}, D(G(z,y),y): {:.4f}'.format(d_pred_real.mean(), d_pred_fake.mean()))

        return
    
    @staticmethod
    def _step(epoch, n_batch, num_batches):
        return epoch * num_batches + n_batch

    @staticmethod
    def _make_dir(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        pass