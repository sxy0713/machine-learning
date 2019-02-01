'''
Created on 2019年1月31日

@author: sxy0713
'''
import numpy as np
if __name__ == '__main__':
    #===========================================================================
    # NumPy - 数组上的迭代
    # NumPy 包包含一个迭代器对象numpy.nditer。 它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。 数组的每个元素可使用 Python 的标准Iterator接口来访问。
    #===========================================================================
    a = np.arange(0,60,5) 
    a = a.reshape(3,4)  
    print ('原始数组是：')  
    print (a) 
    print ('\n')  
    print ('修改后的数组是：')  
    for x in np.nditer(a):  
        print(x)
    # 转置
    b = a.T 
    print (b) 
    print  ('\n')  
    print  ('修改后的数组是：')  
    for x in np.nditer(b):  
        print (x,)
        
        
    print  ('以 C 风格顺序排序：') 
    c = b.copy(order='C')  
    print (c) 
    for x in np.nditer(c):  
        print (x,)  
    print  ('\n')  
    print  ('以 F 风格顺序排序：') 
    c = b.copy(order='F')  
    print (c) 
    for x in np.nditer(c):  
        print (x,)

    #可以通过显式提醒，来强制nditer对象使用某种顺序：
    print  ('以 C 风格顺序排序：')  
    for x in np.nditer(a, order = 'C'):  
        print (x,)  
    print  ('\n')  
    print  ('以 F 风格顺序排序：')  
    for x in np.nditer(a, order = 'F'):  
        print (x,)
    
    #修改数组的值
    #nditer对象有另一个可选参数op_flags。 其默认值为只读，但可以设置为读写或只写模式。 这将允许使用此迭代器修改数组元素。
    for x in np.nditer(a, op_flags=['readwrite']): 
        x[...] = 2 * x 
    print ('修改后的数组是：')  
    print (a) 

    #迭代器遍历对应于每列的一维数组
    print  ('\n')  
    print  ('迭代器遍历对应于每列的一维数组：')  
    for x in np.nditer(a, flags = ['external_loop'], order = 'F'):  
        print (x,)
    
    #如果两个数组是可广播的, 数组b被广播到a的大小
    print  ('\n')  
    print  ('第二个数组：') 
    b = np.array([1,  2,  3,  4], dtype =  int)  
    print (b) 
    print  ('\n')  
    print  ('修改后的数组是：')  
    for x,y in np.nditer([a,b]):  
        print  ("%d:%d"  %  (x,y),)