# coding=<utf-8>
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, Activation
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# -*- coding: utf-8 -*-
hw = pd.read_csv('C:\datamining\project\전년도_65세이상인구비율2.csv', encoding='CP949')
hw = hw.fillna(0)

year=np.array(range(2011,2021)) #2011~2020년

location = input("지역 입력: ")
data = hw[hw['행정구역'].str.contains(location)]

exam = data.iloc[:, 2:]
exam=np.array(exam)
print(exam)

exam=exam.reshape(-1,1)
year=year.reshape(-1,1)


line_fit = LinearRegression()
line_fit.fit(year,exam)
y_predicted =line_fit.predict(year)

print(data.filter(['행정구역']))
print('기울기 :',line_fit.coef_) #기울기
print('y 절편 :',line_fit.intercept_) # 절편

plt.plot(year,exam,'o')
plt.plot(year,y_predicted)
plt.show()