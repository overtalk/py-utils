from numpy import *


# 数组
arr1 = array((1, 23, 54, 78))
arr_n = array([[1, 23, 54, 78], [1, 23, 54, 78], [1, 23, 54, 78]])
print("一维数组 = ", arr1)
print("多维数组 = ", arr_n)

# eye 单位矩阵
print("eye函数生成单位矩阵")
unit_matrix = eye(10)
print(unit_matrix)
print("------------")

# zeros
print("zeros函数生成0数组")
unit_matrix = zeros(10)
print(unit_matrix)
print("------------")

# 随机生成
print("随机生成")
print(random.rand(1))
print(random.rand(4, 5))
print("------------")

# 随机矩阵
print("随机矩阵")
print(mat(random.rand(9, 8)))
print("------------")

# 矩阵的逆
print("矩阵的逆")
rand_mat = mat(random.rand(3, 4))
opposite_rand_mat = rand_mat.I
print(rand_mat)
print(opposite_rand_mat)
print(rand_mat*opposite_rand_mat)
print("------------")


# 矩阵的转制
print("矩阵的转制")
rand_mat = mat(random.rand(3, 4))
opposite_rand_mat = rand_mat.T
print(rand_mat)
print(opposite_rand_mat)
print(rand_mat*opposite_rand_mat)
print("------------")

