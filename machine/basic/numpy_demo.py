from numpy import *


def a():
    # 一维数组
    aa = array((1, 2, 4, 5))
    mm = array((0.1, 0.2, 0.4, 0.5))
    print(aa+mm)
    print(aa*mm)
    print(aa * 2)
    print(aa ** 2)
    print(aa[0])
    # 两维数组
    bb = array([[1, 2, 3], [4, 5, 6]])
    print(bb)
    print(bb[1][2])


def ma():
    m = mat([1, 2, 3])
    print(m)
    print(m[0, 1])
    print(m.T)
    print(m.T * m)
    print(shape(m))


def rand():
    random_array = random.rand(6, 5)
    print("随机数组：", random_array)
    random_mat = mat(random_array)
    print("数组产生矩阵：", random_mat)
    random_mat_i = random_mat.I
    print("矩阵的逆：", random_mat_i)
    print(random_mat_i * random_mat)
    unit_mat = eye(4)
    print("通过eye函数生产的单位矩阵：", unit_mat)


if __name__ == '__main__':
    a()
    ma()
    rand()
