import torch, argparse
import numpy as np
import RFB_reg
import constant
from matplotlib import pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Radial Based Network')
    parser.add_argument('--lr', default=constant.LEARNING_RATE, type=float, help='learning rate')
    parser.add_argument('--batch_size', default=constant.BATCH_SIZE, type=int, help='batch size')
    parser.add_argument('--epoch', default=constant.MAX_EPOCH, type=int, help='epoch size')
    parser.add_argument('--num_class', default=constant.NUM_CLASS, type=int, help='num labels')
    parser.add_argument('--num_centers', default=constant.NUM_CENTERS, type=int, help='num centers')
    parser.add_argument('--save_dir', default=constant.SAVE_DIR, type=str, help='ckpoint loc')
    parser.add_argument('--result_dir', default=constant.RESULT_DIR, type=str, help='output')
    parser.add_argument('--dataset', default=constant.DATASET, type=str)
    parser.add_argument('--model_name', default=constant.MODEL_NAME, type=str)
    parser.add_argument('--cuda', default=constant.USE_CUDA, type=bool)
    parser.add_argument('--num_features', default=constant.NUM_FEATURES, type=int)
    args = parser.parse_args()

    rbfn = RFB_reg.RBFN(args)
    # rbfn.load_with_given_name('RBFN_cur_best.pkl')
    rbfn.load_model()
    rbfn.plt_compare()
    plt.show()
    '''
    res = np.array(rbfn.test())
    x_ = []
    y_ = []
    for idx, (instance, labels) in enumerate(rbfn.test_data):
        x_.append(float(instance))
        y_.append(float(labels))

    local_count = 0
    # for idx, (instance, labels) in enumerate(rbfn.train_data):
    #     if float(instance) > 8.0:
    #         local_count += 1

    print(local_count)

    x_ = np.array(x_)
    y_ = np.array(y_)

    order = x_.argsort()
    x_ = x_[order]
    y_ = y_[order]
    res = res[order]

    plt.plot(x_, y_, 'b-')
    plt.plot(x_, res, 'r-')
    plt.show()
    '''
