'''
Created on 2019年2月1日

@author: ShenJun
'''
from sklearn import datasets
#引入线性回归模型
from sklearn.linear_model import LinearRegression
if __name__ == '__main__':
    ###引入数据###
    load_data = datasets.load_boston()
    data_X = load_data.data
    data_y = load_data.target
    #(506, 13)data_X共13个特征变量
    print(data_X.shape)
    ###训练数据###
    model = LinearRegression()
    model.fit(data_X,data_y)
    #预测前4个数据
    model.predict(data_X[:4,:])
    ###属性和功能###
    print(model.coef_)  
    print(model.intercept_)
    #得到模型的参数
    print(model.get_params())
    #对训练情况进行打分
    print(model.score(data_X,data_y))
    pass