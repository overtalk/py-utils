from numpy import *
# matplotlib 是python的画图库
import matplotlib.pyplot as plt


def file2matrix(filepath="datingTestSet2.txt"):
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


if __name__ == "__main__":
    show_table()
