import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    # test_idx为测试数据编号
    def plot_decision_regions(X, y, classifier, test_idx = None):
        #print("helloworld")
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'grey', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])
        
        # plot the decision region
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.02), np.arange(x2_min, x2_max, 0.02))
        z = classifier.predict(np.array([xx1.flatten(), xx2.flatten()]).T)
        z = z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, z, cmap = cmap, alpha = 0.3)
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)
        
        # plot class samples
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x = X[y == cl, 0], y = X[y == cl, 1], cmap = cmap(idx), marker = markers[idx], label = cl, alpha = 1)
        
        if test_idx:
            X_test, y_test = X[test_idx, :], y[test_idx]
            plt.scatter(X_test[:, 0], X_test[:, 1], c = 'cyan', alpha = 1.0, linewidth = 1, marker = '^', s = 55, label = 'test set')
            plt.legend(loc='best')
            plt.title('Adaline-梯度下降法', fontproperties='SimHei')
            plt.xlabel('经标准化处理的萼片宽度', fontproperties='SimHei')
            plt.ylabel('经标准化处理的花瓣宽度', fontproperties='SimHei')
        
        iris = datasets.load_iris()
        X = iris.data[:, [2, 3]]  # 维度：(150,2)
        y = iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)
        
        sc = StandardScaler()
        sc.fit(X_train)  # 计算训练数据的均值和标准差
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)
        
        X_combined_std = np.vstack((X_train_std, X_test_std))
        y_combined = np.hstack((y_train, y_test))
        LR = LogisticRegression(C = 1000.0, random_state = 0)
        LR.fit(X_train_std, y_train)
        
        plot_decision_regions(X = X_combined_std,
                              y = y_combined,
                              classifier = LR,
                              test_idx = range(105, 150))
        
        print(LR.predict_proba(X_test_std[0:2, :]))  
        
        ''' 
                        权重向量
                        
        '''
        print(LR.coef_)
        
        '''
                        截距项
        '''
        print(LR.intercept_)
        
        print('Test Accuracy:', LR.score(X_test_std, y_test))
        
        plt.show()
        
        
        
        
        
        