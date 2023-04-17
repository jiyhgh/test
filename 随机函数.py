"""
*_* coding: utf-8 *_*
author:ymy
time:2022/11/18 10:25
file :随机函数.py
"""
import numpy as np
a = np.array([[1, 2, 3, 4, 5], [7, 77, 8, 90, 67]])
print(a)
b = np.resize(a, (3, 10))
print(b)
a.resize((3, 10), refcheck=False)
print(a)
# 在数据末尾添加元素，和原数组保持个数相同，不指定类型默认是一维
a1 = np.array([[1, 3, 4]])
print(a1)
print('添加元素', np.append(a1, [2, 4, 5]))
# 指定行元素
print('添加行元素', np.append(a1, [[2, 30, 4]], axis=0))
# 指定列元素
print('添加列元素', np.append(a1, [[30, 45, 6]], axis=1))
# insert插入
a2 = np.array([[1, 2, 3], [2, 3, 5]])
b1 = np.insert(a2, 1, 9, axis=0)
print(b1)
# 在索引后面相对应的列加上指定的元素
b2 = np.insert(a2, 2, 3, axis=1)
print(b2)

#
a3 = np.arange(12).reshape(3, 4)
print(a3)
print('不提供axis参数')
print(np.delete(a3, 5))
# 设置行
print(np.delete(a3, 1, axis=0))
# print(np.delete(a3, [2, 3], axis=0))   # 不能切片
# 设置列
print(np.delete(a3, 1, axis=1))
# np.argwhere 该函数返回的数组中非0元素的索引







