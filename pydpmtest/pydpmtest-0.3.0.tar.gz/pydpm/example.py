## Create Probabilistic Model
from _model import PGBN

# create the model and deploy it on gpu or cpu
model = PGBN([128, 64, 32], device='gpu')
model.initial(train_data)
train_local_params = model.train(100, train_data)
train_local_params = model.test(100, train_data)
test_local_params = model.test(100, test_data)


## Sample on GPU
from _sampler import Basic_Sampler

sampler = Basic_Sampler('gpu')
a = sampler.gamma(np.ones(100)*5, 1, times=10)
b = sampler.gamma(np.ones([100, 100])*5, 1, times=10)
