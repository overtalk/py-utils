from numpy import array, tile, mat
import operator


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def main():
    group, labels = create_data_set()
    c = classify([0, 0], group, labels, 3)
    print(c)


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


if __name__ == '__main__':
    main()
