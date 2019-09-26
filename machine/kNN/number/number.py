from numpy import *
from os import listdir
import operator


def classify(in_x: list, data_set: mat, labels: list, k: int):
    # shape : 矩阵或者数组取其行数，获得样本数量
    data_set_size = data_set.shape[0]
    # tile : 重复，tile(in_x, (data_set_size, 1))的含义就是将in_X重复样本数量份
    # 再减去data_set，就可以得到每个属性的差值
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    # 平方
    sq_diff_mat = diff_mat ** 2
    # 所有距离平方求和
    sq_distances = sq_diff_mat.sum(axis=1)
    # 开方得到距离
    distances = sq_distances ** 0.5
    # 生序排列
    sorted_distances = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_distances[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def img2vector(file_name: str):
    return_vect = zeros((1, 1024))
    f = open(file_name)
    for i in range(32):
        lint_str = f.readline()
        for j in range(32):
            return_vect[0, 32*i+j] = int(lint_str[j])
    return return_vect


def hand_write_class_test():
    hw_labels = []
    # train
    train_file_list = listdir('digits/trainingDigits')
    m = len(train_file_list)
    train_mat = zeros((m, 1024))
    for i in range(m):
        file_name_str = train_file_list[i]
        file_str = file_name_str.split('_')[0]
        class_num_str = int(file_name_str.split('_')[0])
        hw_labels.append(class_num_str)
        train_mat[i, :] = img2vector('digits/trainingDigits/%s' % file_name_str)
    # test
    test_file_list = listdir('digits/testDigits')
    m_test = len(test_file_list)
    error_num = 0.0
    for i in range(m_test):
        file_name_str = test_file_list[i]
        file_str = file_name_str.split('_')[0]
        class_num_str = int(file_name_str.split('_')[0])
        test_mat = img2vector('digits/testDigits/%s' % file_name_str)
        classify_result = classify(test_mat, train_mat, hw_labels, 3)
        print("classify result come back with %d, the real answer is %d, [%d]"
              % (classify_result, class_num_str, classify_result is class_num_str))
        if classify_result is not class_num_str:
            error_num += 1.0
    print("total error rate is %f" % (error_num / m_test))


if __name__ == "__main__":
    hand_write_class_test()
