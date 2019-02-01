'''
Created on 2019年2月1日

@author: sxy0713
'''

import numpy as np
from matplotlib import pyplot as plt 

if __name__ == '__main__':
    #===========================================================================
    # NumPy - 数组操作
    #===========================================================================
    a = np.arange(8)
    print ('原始数组：')
    print (a)
    print ('\n')
     
    b = a.reshape(4,2)
    print ('修改后的数组：')
    print (b)
    
    #numpy.ndarray.flat
    #该函数返回数组上的一维迭代器，行为类似 Python 内建的迭代器。
    a = np.arange(8).reshape(2,4) 
    print ('调用 flat 函数之后：') 
    # 返回展开数组中的下标的对应元素 
    print (a.flat[5])
    
    #numpy.ndarray.flatten
    #该函数返回折叠为一维的数组副本
    #order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。
    print ('展开的数组：') 
    print (a.flatten()) 
    print ('\n')  
     
    print ('以 F 风格顺序展开的数组：') 
    print (a.flatten(order = 'F'))
    
    #numpy.ravel
    #这个函数返回展开的一维数组，并且按需生成副本。返回的数组和输入数组拥有相同数据类型
    print ('调用 ravel 函数之后：') 
    print (a.ravel())  
    print ('\n') 
     
    print ('以 F 风格顺序调用 ravel 函数之后：') 
    print (a.ravel(order = 'F'))

    #===========================================================================
    # 翻转操作
    #===========================================================================
    print ('转置数组：') 
    print (np.transpose(a))
    print ('转置数组：') 
    print (a.T)
    
    #numpy.rollaxis
    #该函数向后滚动特定的轴，直到一个特定位置
    #numpy.rollaxis(arr, saxis, start)
    #arr：输入数组
    #axis：要向后滚动的轴，其它轴的相对位置不会改变
    #start：默认为零，表示完整的滚动。会滚动到特定位置。
    a = np.arange(8).reshape(2,2,2) 
 
    print ('原数组：' )
    print (a) 
    print ('\n')
    # 将轴 2 滚动到轴 0（宽度到深度）
     
    print ('调用 rollaxis 函数：') 
    print (np.rollaxis(a,2))  
    # 将轴 0 滚动到轴 1：（宽度到高度）
    print ('\n') 
     
    print ('调用 rollaxis 函数：') 
    print (np.rollaxis(a,2,1))
    
    #numpy.swapaxes
    #该函数交换数组的两个轴
    #numpy.swapaxes(arr, axis1, axis2)
    #arr：要交换其轴的输入数组
    #axis1：对应第一个轴的整数
    #axis2：对应第二个轴的整数
    # 现在交换轴 0（深度方向）到轴 2（宽度方向）
    print ('调用 swapaxes 函数后的数组：') 
    print (np.swapaxes(a, 2, 0))
    
    #===========================================================================
    # 修改维度
    #===========================================================================
    x = np.array([[1], [2], [3]]) 
    y = np.array([4, 5, 6]) 
    # 对 y 广播 x
    z = np.broadcast(x,y)  
    print ('广播对象的形状：') 
    print (z.shape) 
    print ('\n')  
    # 它拥有 iterator 属性，基于自身组件的迭代器元组
    print ('对 y 广播 x：') 
    r,c = z.iters
    print (r.__next__(), c.__next__()) #原因是在python 3.x中 generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了,
    print (r.__next__(), c.__next__()) #next是python 3.x以前版本中的方法
    # 手动使用 broadcast 将 x 与 y 相加
    b = np.broadcast(x,y) 
    c = np.empty(b.shape)
    print ('手动使用 broadcast 将 x 与 y 相加：') 
    print (c.shape) 
    print ('\n')  
    c.flat = [u + v for (u,v) in b]
    print ('调用 flat 函数：') 
    print (c) 
    print ('\n')  
    # 获得了和 NumPy 内建的广播支持相同的结果
    print ('x 与 y 的和：') 
    print (x + y)
    
    
    x = np.arange(1,11) 
    y =  2  * x +  5 
    plt.title("Matplotlib demo") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    plt.plot(x,y)
    plt.show()

    pass