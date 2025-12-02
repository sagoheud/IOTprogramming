import matplotlib.pylab as plt
from sklearn import linear_model # pip install scikit-learn

reg = linear_model.LinearRegression()

x = [[1.0],[2.0],[3.0],[4.0],[5.0]] # 학습 데이터
y = [[1.0],[2.0],[1.6],[3.8],[2.3]] # 결과 데이터
reg.fit(x,y) # 학습

# 학습 데이터와 y 값을 산포도로 그린다
plt.scatter(x, y, color='black') 

# 학습 데이터를 입력으로 하여 예측값을 계산한다
y_pred = reg.predict(x)

# 학습 데이터와 예측값으로 선그래프로 그린다. 
# 계산된 기울기와 y 절편을 가지는 직선이 그려진다. 
plt.plot(x, y_pred, color='blue', linewidth=3)
plt.show()