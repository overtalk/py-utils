import sys
sys.path.append('..')
from numpy import *
from os import listdir
from dating.demo import classify


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
