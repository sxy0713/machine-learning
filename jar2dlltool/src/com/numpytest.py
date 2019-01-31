'''
Created on 2019年1月31日

@author: ShenJun

'''
import numpy as np

if __name__ == '__main__':
    
    #===========================================================================
    # NumPy - Ndarray 对象
    #===========================================================================
    
    # 首先创建结构化数据类型。  
    dt = np.dtype([('age',np.int8)]) 
    # 现在将其应用于 ndarray 对象 
    a = np.array([(10,),(20,),(30,)], dtype = dt)  
    print(a)
    # 文件名称可用于访问 age列的内容
    print (a['age'])
    
    student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])  
    print(student)
    
    student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')]) 
    a = np.array([('abc',  21,  50),('xyz',  18,  75)], dtype = student)  
    print (a)
    
    #===========================================================================
    # 
    # NumPy - 数组属性
    #===========================================================================
    #这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
    a = np.array([[1,2,3],[4,5,6]])  
    print(a.shape)
    
    # 这会调整数组大小
    a = np.array([[1,2,3],[4,5,6]]) 
    a.shape =  (3,2) 
    print(a) 
    
    #reshape函数来调整数组大小
    b = a.reshape(3,2)
    print(b) 
    print(b.ndim)
    
    # 数组的 dtype 为 int8（一个字节）  
    x = np.array([1,2,3,4,5], dtype = np.int8)  
    y = np.array([1,2,3,4,5], dtype = np.float32)
    print (x.itemsize)
    print (y.itemsize)
    
    # 展示当前的标志
    print(x.flags)
    
    #===========================================================================
    # NumPy - 数组创建例程
    #===========================================================================
    z = np.empty([3,2], dtype = int)  
    print(z)

    z = np.zeros((5,), dtype = np.int)
    print(z)
    
    # 自定义类型 
    z = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'i4')])
    print(z)
    
    z = np.ones(5)
    print(z)
    
    z = np.ones([2, 2], dtype = int)
    print(z)
    
    #===========================================================================
    # NumPy - 来自现有数据的数组
    #===========================================================================
    #将列表转换为 ndarray 
    x =  [1,2,3] 
    a = np.asarray(x)  
    print(a)
    a = np.asarray(x, dtype = float)  
    print(a)
    
    ## 来自元组列表的 ndarray
    x =  (1,2,3) 
    a = np.asarray(x)  
    print(a)

    x =  [(1,2,3),(4,5)] 
    a = np.asarray(x)  
    print(a)
    
    
    
    pass