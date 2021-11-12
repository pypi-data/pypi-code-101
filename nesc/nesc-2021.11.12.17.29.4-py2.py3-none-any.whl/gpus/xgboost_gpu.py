import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 创建数据集
dataset, labels = make_classification(n_samples=10000, n_features=50, n_informative=3, n_classes=3)
print(dataset.shape, labels.shape)
# 拆分数据集
x_train, x_test, y_train, y_test = train_test_split(dataset, labels, test_size=0.3, random_state=7)
print("x_train: {}, x_test: {}".format(x_train.shape, x_test.shape))

# 构建DMatrix
dtrain = xgb.DMatrix(x_train, y_train)
dtest = xgb.DMatrix(x_test, y_test)

param = {'objective': 'multi:softmax', # Specify multiclass classification
         'num_class': 8, # Number of possible output classes
         'tree_method': 'gpu_hist' # Use GPU accelerated algorithm
         }
# 参数设置
params = {
        'tree_method': "gpu_hist",
        'booster': 'gbtree',
        'objective': 'multi:softmax',
        'num_class': 3,
        'max_depth': 6,
        'eval_metric': 'merror',
        'eta': 0.01,
        # 'gpu_id': cr.gpu_id
    }

# 训练
evals = [(dtrain, 'train'), (dtest, 'val')]
model = xgb.train(params, dtrain, num_boost_round=100000,
                  evals=evals)
