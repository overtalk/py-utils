from numpy import *
# matplotlib 是python的画图库
import matplotlib.pyplot as plt
from demo import classify


def file2matrix(filepath: str ="datingTestSet2.txt"):
    f = open(filepath)
    lines = f.readlines()
    number_of_lines = len(lines)
    # 定义返回数据
    return_mat = zeros((number_of_lines, 3))
    return_labels = []
    index = 0
    for line in lines:
        # strip方法用于移除字符串头尾指定的字符（默认为空格）或字符序列
        line = line.strip()
        # 分割字符串，得到list
        line_data = line.split('\t')
        return_mat[index, :] = line_data[0:3]
        return_labels.append(int(line_data[-1]))
        index += 1
    return return_mat, return_labels


def show_table():
    dating_mat, dating_labels = file2matrix()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dating_mat[:, 1], dating_mat[:, 2],
               15.0*array(dating_labels), 15.0*array(dating_labels))
    plt.show()


def auto_norm(data_set: asmatrix):
    min_val = data_set.min(0)
    max_val = data_set.max(0)
    val_range = max_val - min_val
    normal_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    normal_data_set = data_set - tile(min_val, (m, 1))
    normal_data_set = normal_data_set/tile(val_range, (m, 1))
    return normal_data_set, val_range, min_val


def dating_class_test():
    ho_ratio = 0.10
    dating_mat, dating_labels = file2matrix()
    normal_data_set, val_range, min_val = auto_norm(dating_mat)
    m = normal_data_set.shape[0]
    num_test_vecs = int(m * ho_ratio)
    error_count = 0.0
    for i in range(num_test_vecs):
        classify_result = classify(normal_data_set[i, :], normal_data_set[num_test_vecs: m, :],
                 dating_labels[num_test_vecs:m], 3)
        print("the classify result come back with %d, the real result is %d --- %d"
              % (classify_result, dating_labels[i], classify_result is not dating_labels[i]))
        if classify_result is not dating_labels[i]: error_count += 1.0
    print("total error rate is %f" % (error_count/num_test_vecs))


if __name__ == "__main__":
    dating_class_test()
