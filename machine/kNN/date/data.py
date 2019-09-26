import sys
sys.path.append('..')
from numpy import *
from ..classify import classify


# 从文件中读取出数据
def txt2matrix(filepath: str ="datingTestSet2.txt"):
    f = open(filepath)
    lines = f.readlines()

    # m 表示样本数据量
    m = len(lines)

    # 构造返回数据（mat & label）
    return_mat = zeros((m, 3))
    return_labels = []

    index = 0
    for line in lines:
        line = line.strip()
        slices = line.split('\t')
        return_mat[index, :] = slices[:3]
        return_labels.append(int(slices[-1]))
        index += 1

    return return_mat, return_labels


# 百分比化
def auto_norm(data_set):
    # 数据集大小
    m = data_set.shape[0]

    min_val = data_set.min(0)
    max_val = data_set.max(0)
    interval = max_val - min_val

    normal_data_set = data_set - tile(min_val, [m, 1])
    normal_data_set = normal_data_set/tile(interval, [m, 1])
    return normal_data_set


# 使用数据进行测试
def date_test():
    todo_mat, todo_labels = txt2matrix()
    normal_mat = auto_norm(todo_mat)
    m = todo_mat.shape[0]

    # 用于测试的case数量
    test_num = int(m * 0.1)
    error_count = 0.0
    for i in range(test_num):
        classify_result = classify(normal_mat[i, :], normal_mat[test_num:m, :], todo_labels[test_num:m], 3)
        is_expected = classify_result is todo_labels[i]
        print("classify result is %d, real result is %d --- [%d]" % (classify_result, todo_labels[i], is_expected))
        if not is_expected:
            error_count += 1.0
    print("error rate : %f" % (error_count/test_num))


if __name__ == "__main__":
    date_test()



