'''
Created on 2019年2月2日

@author: ShenJun
'''
from sklearn import preprocessing
import numpy as np
import pandas as pd
if __name__ == '__main__':
    X = np.array([[1., -1, 2,],
                 [2., 0., 0.],
                 [0., 1., -1.]])
    X_scaled = preprocessing.scale(X)
    print(X_scaled)
    
    print(X_scaled.mean(axis = 0))
    print(X_scaled.std(axis = 0))
    
    scaler = preprocessing.StandardScaler().fit(X)
    print(scaler)
    print(scaler.mean_)
    print(scaler.scale_)
    print(scaler.transform(X))
    print(scaler.transform([[-1., 1., 0.]]))
    
    pass