import numpy as np
import argparse
import constant
import RFB_reg
import table_reader
import preprocessing

THREE_DIMENSIONS = [
    [3, 23],        # 综合指数需要所有特征
    [3, 13],        # 表格中从第3列至第13列为自然信息维度相关特征
    [14, 19],       # 表格中从第14列至第19列为动能信息维度相关特征
    [20, 23]        # 表格中从第20列至第23列为价值信息维度相关特征
]

MODEL_NAME = [
    'overall_rating',
    'first_dimension',
    'second_dimension',
    'third_dimension'
]


if __name__ == '__main__':
    # 工作模式：
    #           0，综合指数
    #           1, 自然信息维度
    #           2，动能信息维度
    #           3，价值信息维度
    working_mode = 0    # 此处示例为综合指数

    # 切换训练/评分模式，1为训练模式，0为评分模式
    # 训练模式下程序会根据下方配置的参数，参考提供的数据得出合适的评分模型
    # 评分模式下程序使用训练得到的模型进行评分 给出相应结果
    is_training = 1     # 此处示例为评分模式

    # 根据所选模式做一些基础的参数配置
    num_features = THREE_DIMENSIONS[working_mode][1] - THREE_DIMENSIONS[working_mode][0] + 1
    model_name = MODEL_NAME[working_mode]

    print('Start Configuration')

    ''' ****************** 网络相关参数加载 ****************** '''
    # 网络名称
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
    parser.add_argument('--epoch', default=2000, type=int, help='epoch size')

    # 此处class数量应当为1，因为当前处理的问题为回归问题
    parser.add_argument('--num_class', default=constant.NUM_CLASS, type=int, help='num labels')

    # 隐含层节点数量 数量越多网络参数就越多 能够应对更复杂的数学模型
    parser.add_argument('--num_centers', default=constant.NUM_CENTERS, type=int, help='num centers')

    # 最终输出模型的保存目录
    parser.add_argument('--save_dir', default=constant.SAVE_DIR, type=str, help='ckpoint loc')

    # 数据集名称
    parser.add_argument('--dataset', default="samples", type=str)

    # manually = False：自动模式，根据dataset字段中提供的数据位置加载数据
    # manually = True:  手动模式，手动加载数据，可根据需要提前做一些预处理
    parser.add_argument('--manually', default=True, type=bool)

    # 模型名称，最终输出模型的保存目录为./save_dir/dataset/model_name
    parser.add_argument('--model_name', default=model_name, type=str)

    # 是否启用GPU加速
    parser.add_argument('--cuda', default=constant.USE_CUDA, type=bool)

    # 特征数
    parser.add_argument('--num_features', default=num_features, type=int)
    args = parser.parse_args()
    ''' ****************** 参数配置加载完毕 ****************** '''

    print('Configuration Done!')

    rbfn = RFB_reg.RBFN(args)

    # 高维度数据不支持可视化，仅2维及3维数据支持可视化
    rbfn.set_visualize_mode(False)

    """ *********************   加载数据集   ********************* """

    print('Start Loading Dataset')

    m_table = table_reader.TableReader('data/sample.xlsx', 4)   # 表格中的第4页为目标信息
    m_table.load_attr_in_table(3)   # 表格中的第3行为相关特征名称
    m_table.excel2list()

    # print(m_table.table_list)
    table_array = np.array(m_table.table_list)

    # 数据用于训练前需要做预处理
    processed_array = preprocessing.pre_processing(table_array, working_mode, THREE_DIMENSIONS[working_mode])

    for idx in range(num_features):
        # First two rows are removed, cause they are irrelevant to the task
        print("attr: {}, idx: {}".format(m_table.get_attr()[idx+2], idx))
        print("max: {}; min: {}".format(np.max(processed_array[:, idx]), np.min(processed_array[:, idx])))
        print()

    score_arr = np.sum(processed_array, axis=1)
    score_arr = score_arr.reshape(len(score_arr), 1)

    print(score_arr)
    print("max Score: [{:>.4}]; min Score: [{:>.4}]".format(np.max(score_arr), np.min(score_arr)))

    print(np.shape(score_arr), np.shape(table_array))

    res = np.column_stack((processed_array, score_arr))
    print('Loading Dataset Done')
    """
    *********************   数据集加载完成   *********************
    """

    print('Initializing Rating model')

    rating = None

    if is_training:
        print("Entering Training Phase!")

        # 训练模式下需要打乱数据顺序，引入随机性，以此保证模型可以正常收敛
        np.random.shuffle(res)

        # 加载数据集的同时对模型进行初始化
        rbfn.load_training(res)
        # 模型初始化时需要参考数据集内部分数据，因此需要在加载数据后再进行初始化
        rbfn.init_model()

        # 训练模型，直至满足上述参数配置中的收敛条件
        rbfn.train()

        print('Training Done!')

        # 保存模型
        rbfn.save_model()

        # 确保保存后的模型可以正常加载
        rbfn.load_model()
        rbfn.load_testing(res)
        rating = rbfn.test()
    else:
        print('Entering Rating Phase!')
        # 加载数据集的同时对模型进行初始化
        rbfn.load_training(res)
        # 模型初始化时需要参考数据集内部分数据，因此需要在加载数据后再进行初始化
        rbfn.init_model()

        # 输入待评分数据
        test_instance = np.array([
            ['教师', '孔子',  # this two won't be used in rating
             3, 72, 3, 170, 73, 6, 6, 5, 0, 5, 0, 10, 4, 0.001, 9, 10, 10, 10, 3, 500000, 7],
            ['Engineer', 'cjh',  # this two won't be used in rating
             3, 25, 2, 170, 74, 6, 8, 5, 0, 5, 0, 4,  2, 0.1,   7, 6,  8,  1,  2, 2,      0]
                                  ])    # 一次性可以输入多个待评分的条目

        # 数据预处理，整理为适用于网络输入的格式
        test_instance.reshape(len(test_instance), len(test_instance[0]))

        test_instance = preprocessing.pre_processing(test_instance, working_mode, THREE_DIMENSIONS[working_mode])

        # 网络的输入为 特征+评分，其中评分值只在训练时会用到，因此此处全部补0即可
        score_arr = np.zeros(len(test_instance))
        score_arr = score_arr.reshape(len(score_arr), 1)

        test_instance = np.column_stack((test_instance, score_arr))

        print(np.shape(test_instance))

        # 根据给定的配置信息，在指定位置找到模型文件并加载网络
        rbfn.load_model()

        # 将需要评分的数据作为网络的输入
        rbfn.load_testing(test_instance)

        # 获取评分结果
        rating = rbfn.test()

        print('Rating done')
    rating = np.array(rating)

    bound_low = 27.
    bound_high = 68.
    if working_mode != 0:
        bound_low = 0.
        bound_high = 30.

    rating = preprocessing.re_ranging(rating, [0., 1000000.], [bound_low, bound_high])
    rating = preprocessing.post_processing(rating, 0., 1000000.)

    for i in range(len(rating)):
        print("Rating: [{:>6}]".format(int(rating[i])))
    print("[Prediction] Max: {:>6}; Min: {:>6}".format(int(np.max(rating)), int(np.min(rating))))
