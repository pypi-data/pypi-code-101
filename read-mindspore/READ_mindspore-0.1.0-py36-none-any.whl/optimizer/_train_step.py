import mindspore.nn as nn
import mindspore.ops as P
import mindspore
import mindspore.ops.functional as F
import mindspore.ops.composite as C

class WithLossCell(nn.Cell):
    def __init__(self, network):
        super(WithLossCell, self).__init__(auto_prefix=False)
        self.network = network

    def construct(self, img):
        loss, _ = self.network(img)
        return loss

class TrainOneStepCell(nn.Cell):
    def __init__(self,
                 net_with_all_loss,
                 net_with_only_output,
                 optimizer: nn.Optimizer,
                 sens=1.0,
                 auto_prefix=True):

        super(TrainOneStepCell, self).__init__(auto_prefix=auto_prefix)
        self.net_with_all_loss = net_with_all_loss
        self.net_with_all_loss.add_flags(defer_inline=True)
        self.net = WithLossCell(net_with_all_loss)
        self.weights = mindspore.ParameterTuple(net_with_only_output.trainable_params())
        self.optimizer = optimizer
        self.grad = C.GradOperation(get_by_list=True, sens_param=True)
        self.sens = sens


    def train(self, real_data, loss):
        sens = P.Fill()(P.DType()(loss), P.Shape()(loss), self.sens)
        grad_ops = self.grad(self.net, self.weights)
        grads = grad_ops(real_data, sens)
        return F.depend(loss, self.optimizer(grads))

    def construct(self, real_data):
        loss, loss_lst = self.net_with_all_loss(real_data)
        print(loss.shape)
        out = self.train(real_data, loss)
        return loss, loss_lst

class WithLossCellTwoParameters(nn.Cell):
    def __init__(self, network):
        super(WithLossCellTwoParameters, self).__init__(auto_prefix=False)
        self.network = network

    def construct(self, img_A, img_B):
        loss, _ = self.network(img_A, img_B)
        return loss

class TrainOneStepCellTwoParameters(nn.Cell):
    def __init__(self,
                 net_with_all_loss,
                 net_with_only_output,
                 optimizer: nn.Optimizer,
                 sens=1.0,
                 auto_prefix=True):

        super(TrainOneStepCellTwoParameters, self).__init__(auto_prefix=auto_prefix)
        self.net_with_all_loss = net_with_all_loss
        self.net_with_all_loss.set_grad()
        self.net_with_all_loss.add_flags(defer_inline=True)
        self.net = WithLossCellTwoParameters(net_with_all_loss)
        self.weights = mindspore.ParameterTuple(net_with_only_output.trainable_params())
        self.optimizer = optimizer
        self.grad = C.GradOperation(get_by_list=True, sens_param=True)
        self.sens = sens


    def train(self, t_data, s_data, loss):
        sens = P.Fill()(P.DType()(loss), P.Shape()(loss), self.sens)
        grad_ops = self.grad(self.net, self.weights)
        grads = grad_ops(t_data, s_data, sens)
        return F.depend(loss, self.optimizer(grads))

    def construct(self, t_data, s_data):
        loss, loss_lst = self.net_with_all_loss(t_data, s_data)
        out = self.train(t_data, s_data, loss)
        return loss, loss_lst
