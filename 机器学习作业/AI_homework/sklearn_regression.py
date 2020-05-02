#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt


#1.首先生成数据


def f(x1, x2):
    y = 2 * np.sin(x1) + 5 * np.cos(x2) +2*np.exp(0.001*(x1+x2))+ 3 + 0.1 * x1
    return y


def load_data():
    x1_train = np.linspace(0,80,800)
    x2_train = np.linspace(-20,20,800)
    data_train = np.array([[x1,x2,f(x1,x2) + (np.random.random(1)-0.5)] for x1,x2 in zip(x1_train, x2_train)])
# 训练的数据要加入噪声
    x1_test = np.linspace(0,80,800)+ 0.5 * np.random.random(800)
    x2_test = np.linspace(-20,20,800) + 0.02 * np.random.random(800)
    data_test = np.array([[x1,x2,f(x1,x2)] for x1,x2 in zip(x1_test, x2_test)])
# 测试的数据没有噪声
    return data_train, data_test


train, test = load_data()
x_train, y_train = train[:,:2], train[:,2] 
#上面的数据前两列是x1,x2 第三列是y,这里的y有随机噪声
x_test ,y_test = test[:,:2], test[:,2] 
# 上面的数据前两列是x1,x2 第三列是y,这里的y没有随机噪声


#2.回归部分


def convert_to_str(model):
    i =0;
    str1=str(model);
    while str1[i]!='(':
        i+=1
    return str1[:i]


def regression(model):
    model.fit(x_train,y_train)
    score = model.score(x_test, y_test)
    result = model.predict(x_test)
    fig1=plt.figure(dpi=100)
    plt.plot(0.8*np.arange(len(result)), y_test,color="blue",label='true value')
    plt.plot(0.8*np.arange(len(result)),result,color="red",label='predict value')
    title=convert_to_str(model)
    plt.title(title+'  Score: {0:^20.9f}'.format(score))
    plt.grid()
    plt.legend()
    plt.savefig(fname=title,dpi=250,forma='png')
    plt.show()
    

    
#3.具体方法选择


#3.1决策树回归

from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()

#3.2线性回归

from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()

#3.3SVM回归

from sklearn import svm
model_SVR = svm.SVR()

#3.4KNN回归

from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()

#3.5随机森林回归

from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)
#这里使用20个决策树

#3.6Adaboost回归

from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)
#这里使用50个决策树

#3.7GBRT回归

from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)
#这里使用100个决策树

#3.8Bagging回归

from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()

#3.9ExtraTree极端随机树回归

from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()


#4.具体方法调用部分


regression(model_DecisionTreeRegressor)
regression(model_LinearRegression)
regression(model_SVR)
regression(model_KNeighborsRegressor)
regression(model_RandomForestRegressor)
regression(model_AdaBoostRegressor)
regression(model_GradientBoostingRegressor)
regression(model_BaggingRegressor)
regression(model_ExtraTreeRegressor)


# In[ ]:




