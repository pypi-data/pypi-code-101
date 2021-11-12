# -*- coding: utf-8 -*-
# 导入这两个是为了获取mnist数据集
import tensorflow as tf
mnist=tf.keras.datasets.mnist

# 下面三行是常规导入
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models

#导入mnist数据集，需要保持网络畅通
(X_train, Y_train), (X_test, Y_test) = mnist.load_data(path='/home/jovyan/mnist.npz')

img_rows, img_cols = 28, 28 # 图像的尺寸

# 训练数据;X_train是60000张28*28的数据，所以尺寸是60000*28*28，Y_train是对应的数字，尺寸是60000*1，X_test和Y_test同理
X_train, X_test = X_train / 255.0, X_test / 255.0   # 将图像像素转化为0-1的实数

# 将标准答案通过one-hot编码转化为需要的格式（这两个函数不懂见下个模块的介绍）
Y_train = keras.utils.to_categorical(Y_train, num_classes=10)
Y_test = keras.utils.to_categorical(Y_test, num_classes=10)

# 将训练所用的图像调整尺寸，由于图像是黑白图像，所以最后一维的值是1
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)

###############################
### 使用keras API开始定义模型 ###
###############################
model = models.Sequential()

# 向模型中添加层
model.add(layers.Conv2D(32, kernel_size=(5,5),  # 添加卷积层，深度32，过滤器大小5*5
                        activation='relu',  # 使用relu激活函数
                        input_shape=(img_rows, img_cols, 1)))   # 输入的尺寸就是一张图片的尺寸(28,28,1)
model.add(layers.MaxPooling2D(pool_size=(2, 2)))    # 添加池化层，过滤器大小是2*2
model.add(layers.Conv2D(64, (5,5), activation='relu'))  # 添加卷积层，简单写法
model.add(layers.MaxPooling2D(pool_size=(2, 2)))    # 添加池化层
model.add(layers.Flatten())     # 将池化层的输出拉直，然后作为全连接层的输入
model.add(layers.Dense(500, activation='relu'))     # 添加有500个结点的全连接层，激活函数用relu
model.add(layers.Dense(10, activation='softmax'))   # 输出最终结果，有10个，激活函数用softmax

# 定义损失函数、优化函数、评测方法
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(),
              metrics=['accuracy'])

# 自动完成模型的训练过程
model.fit(X_train, Y_train,   # 训练集
          batch_size=128,   # batchsize
          epochs=20,    # 训练轮数
          validation_data=(X_test, Y_test))   # 验证集

# 打印运行结果，即损失和准确度
score = model.evaluate(X_test, Y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

