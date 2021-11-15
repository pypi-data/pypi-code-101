import numpy as np
import argparse
import constant
import RFB_reg
import table_reader
import preprocessing


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Radial Based Network')

    # lr：  学习率 (learning rate) ，决定个训练周期间反向传播的步长
    #       较大的lr能够加速模型的训练，但是由于步长过大，最终的结果有可能较差，并可能引入一些其他问题
    #       较小的lr会增加训练时的时间开销，不过通常能得到较好的模型
    parser.add_argument('--lr', default=constant.LEARNING_RATE, type=float, help='learning rate')

    # batch_size:   批尺寸，合适的batch size能够提高内存的利用率，并加速训练流程；
    #               若不了解参数设置，建议使用此处的默认值
    parser.add_argument('--batch_size', default=constant.BATCH_SIZE, type=int, help='batch size')

    # epoch:    即maximum epoch，限制最大的迭代次数，避免模型出现过拟合
    #           考虑到当前问题比较简单，通常不会用到该参数
    parser.add_argument('--epoch', default=constant.MAX_EPOCH, type=int, help='epoch size')

    # 此处class数量应当为1，因为当前处理的问题为回归问题
    parser.add_argument('--num_class', default=constant.NUM_CLASS, type=int, help='num labels')
    parser.add_argument('--num_centers', default=constant.NUM_CENTERS, type=int, help='num centers')
    parser.add_argument('--save_dir', default=constant.SAVE_DIR, type=str, help='ckpoint loc')
    parser.add_argument('--dataset', default=constant.DATASET, type=str)

    """ 
    manually = False：自动模式，根据dataset字段中提供的数据位置加载数据
    manually = True:  手动模式，手动加载数据，可根据需要提前做一些预处理
    """
    parser.add_argument('--manually', default=True, type=bool)
    parser.add_argument('--model_name', default=constant.MODEL_NAME, type=str)
    parser.add_argument('--cuda', default=constant.USE_CUDA, type=bool)
    parser.add_argument('--num_features', default=21, type=int)
    args = parser.parse_args()

    rbfn = RFB_reg.RBFN(args)
    rbfn.set_visualize_mode(False)

    """
    *********************   加载数据集   *********************
    """
    m_table = table_reader.TableReader('data/sample.xlsx', 4)
    m_table.load_attr_in_table(3)
    # print(m_table.get_attr())
    # print(m_table.get_instance(0))
    m_table.excel2list()

    # print(m_table.table_list)

    table_array = np.array(m_table.table_list)

    processed_array = preprocessing.pre_processing(table_array, 0, [3, 23])

    for idx in range(len(m_table.get_attr())-2):
        # First two rows are removed, cause they are irrelevant to the task
        print("attr: {}, idx: {}".format(m_table.get_attr()[idx+2], idx))
        print("max: {}; min: {}".format(np.max(processed_array[:, idx]), np.min(processed_array[:, idx])))
        print()

    score_arr = np.sum(processed_array, axis=1)
    score_arr = score_arr.reshape(len(score_arr), 1)

    print(score_arr)
    print("max Score: [{:>.4}]; min Score: [{:>.4}]".format(np.max(score_arr), np.min(score_arr)))

    for i in range(len(score_arr)):
        if np.isnan(score_arr[i]):
            print("------------------ ", table_array[i])
        if score_arr[i] < 0:
            print("------------------ ", table_array[i])

    print(np.shape(score_arr), np.shape(table_array))

    res = np.column_stack((processed_array, score_arr))
    np.random.shuffle(res)


    # res = np.hstack((table_array, score_arr))
    # print(res)
    """
    *********************   数据集加载完成   *********************
    """
    print("Start loading dataset")

    rbfn.load_training(res)
    rbfn.init_model()

    rbfn.train()
    rbfn.save_model()
    rbfn.load_model()
    # rbfn.test()
