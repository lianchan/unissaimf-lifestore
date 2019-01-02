#!/bin/env bash
# -*- encoding:utf-8 -*-
import numpy as np;
import cmath;



a = np.arange(24)
print (a)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)

x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype = np.int)
print(y)

# 自定义类型
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(z)

# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)

m = np.zeros(10000,dtype=int);
print(m)
#等差数列
a = np.linspace(1,200,10,dtype=int)
print(a)
a =np.linspace(1,10,10,retstep= True)

print(a)
# 拓展例子
b =np.linspace(1,10,10).reshape([10,1])
print(b)

print("等比数列")

dbsl = np.logspace(1,300,10,endpoint=False,base=2,dtype=int);

print(dbsl)


a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a + b)

a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('原始数组的转置是：')
b = a.T
print (b)
print ('\n')
print ('以 C 风格顺序排序：')
c = b.copy(order='C')
print (c)
for x in np.nditer(c):
    print (x, end=", " )
print  ('\n')
print  ('以 F 风格顺序排序：')
c = b.copy(order='F')
print (c)
for x in np.nditer(c):
    print (x, end=", " )
print("等比数列")

dbsl = np.logspace(1,300,10,endpoint=False,base=2,dtype=int);

print(dbsl)
