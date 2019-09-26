from numpy import *
import operator
import os


def classify(inX, data_set, data_labels, k):
    # m 表示样本数量
    m = data_set.shape[0]
    mat_diff = data_set - tile(inX, [m, 1])
    sorted_distances = (((mat_diff**2).sum(axis=1))**0.5).argsort()
    label_count = {}
    for i in range(k):
        label = data_labels[sorted_distances[i]]
        label_count[label] = label_count.get(label, 0) + 1
    sorted_class_count = sorted(label_count.items(),
                                key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def txt2array(filepath: str):
    return_array = zeros((1, 1024))
    f = open(filepath)
    lines = f.readlines()
    lines_count = len(lines)

    for i in range(lines_count):
        for j in range(lines_count):
            return_array[0, i*32+j] = int(lines[i][j])
    return return_array


def date_test():
    test_path = 'testDigits'
    train_path = 'trainingDigits'

    # train
    train_files = os.listdir(train_path)
    m = len(train_files)
    # 定义labels，matrix
    train_labels = []
    train_matrix = zeros((m, 1024))
    # 读取文件
    for i in range(m):
        file_name = train_files[i]
        train_labels.append(int(file_name.split('_')[0]))
        train_matrix[i, :] = txt2array(train_path + "/" + file_name)

    # test
    text_files = os.listdir(test_path)
    m = len(text_files)
    error_count = 0.0
    # 读取文件
    for i in range(m):
        file_name = text_files[i]
        text_label = int(file_name.split('_')[0])
        text_matrix = txt2array(test_path + "/" + file_name)
        classify_result = classify(text_matrix, train_matrix, train_labels, 3)
        is_expected = classify_result is text_label
        if not is_expected:
            error_count += 1.0
        print("classify result is %d, real result is %d --- [%d]" % (classify_result, text_label, is_expected))
    print("total error rate is %f" % (error_count / m))


if __name__ == "__main__":
    date_test()