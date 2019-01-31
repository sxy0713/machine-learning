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

