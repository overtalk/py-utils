from numpy import *
import operator


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


def create_data_set():
    return_mat = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    return_labels = ['A', 'A', 'B', 'B']
    return return_mat, return_labels


if __name__ == '__main__':
    group, labels = create_data_set()
    c = classify([0, 0], group, labels, 3)
    print(c)
