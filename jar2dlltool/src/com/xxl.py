'''
Created on 2019年1月10日

@author: shenjun
'''
import os
import re
import numpy as np
#import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("helloworld")
    hello = ""
    f = os.popen(r"D:\soft\ikvm-8.1.5717.0\bin\ikvmc -nologo -out:jar2dlltool.dll D:\java2net\java2netTest.jar", "r")
    
    d = f.read()
    f2 = os.popen(r"dir .", "r")
    d2 = f2.read()
    print(d2)
#     f2 = os.open(r"dir .", flags, mode, dir_fd=None)

#     print("the response is " + d)
#     print(type(d))
#     strlizer = str(d);
#     print(strlizer)
#     compile = re.compile(r'Jeroen')
#     print(re.findall(strlizer, compile))
#     isHasMistaken = re.search(r'I', strlizer)
#     print(isHasMistaken)
    f.close()
    f2.close()
    
    rootdir = 'D:\java2net'
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            print(path)
        
    
