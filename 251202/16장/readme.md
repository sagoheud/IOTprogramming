# 기계학습 & 딥러닝 가이드

Python으로 배우는 기계학습과 딥러닝 완벽 입문서

## 목차
- [기계학습이란?](#기계학습이란)
- [기계학습의 분류](#기계학습의-분류)
- [지도학습](#지도학습)
- [선형 회귀](#선형-회귀)
- [신경망 기초](#신경망-기초)
- [Keras 소개](#keras-소개)
- [XOR 문제 해결](#xor-문제-해결)
- [MNIST 숫자 인식](#mnist-숫자-인식)
- [타이타닉 생존자 예측](#타이타닉-생존자-예측)

## 기계학습이란?

**기계학습(Machine Learning)**은 인공지능의 한 분야로, 컴퓨터에 학습 기능을 부여하기 위한 연구 분야입니다.

### 인공지능, 기계학습, 딥러닝의 관계

```
인공지능 (Artificial Intelligence)
└── 기계학습 (Machine Learning)
    └── 딥러닝 (Deep Learning)
```

### 기계학습의 핵심 개념

기계학습 = 함수 근사(Function Approximation)

```python
y = f(x)  # 입력(x)을 받아 출력(y)을 내는 함수를 학습
```

### 기계학습이 필요한 경우

1. **규칙이 너무 복잡할 때**
   - 음성 인식, 이미지 인식 등

2. **규칙이 지속적으로 변할 때**
   - 보안 시스템의 침입 탐지
   - 신용카드 사기 감지

3. **데이터 특징이 계속 변할 때**
   - 주식 거래 예측
   - 에너지 수요 예측
   - 쇼핑 트렌드 예측

## 기계학습의 분류

### 1. 지도학습 (Supervised Learning)

"교사"가 정답(레이블)을 제공하는 학습

- **회귀(Regression)**: 연속적인 값 예측 (집값, 온도 등)
- **분류(Classification)**: 범주 예측 (스팸/정상, 고양이/개 등)

### 2. 비지도학습 (Unsupervised Learning)

정답 없이 데이터의 패턴을 스스로 발견

- **클러스터링(Clustering)**: 유사한 데이터 그룹화
- **차원 축소**: 데이터 압축 및 시각화

### 3. 강화학습 (Reinforcement Learning)

보상/처벌 피드백으로 학습

- 게임 플레이, 자율주행 등

## 지도학습

### 주요 용어

**특징(Features)**
- 모델에 입력하는 데이터
- 예: 이메일의 특정 단어 포함 여부, 특수문자 개수 등

**레이블(Label)**
- y = f(x)에서 y에 해당
- 예측하고자 하는 정답

**샘플(Sample)**
- 학습에 사용되는 개별 데이터
- y = f(x)에서 x에 해당

### 학습 데이터 vs 테스트 데이터

```
전체 데이터
├── 학습 데이터 (Training Data) - 70~80%
│   └── 모델 학습에 사용
└── 테스트 데이터 (Test Data) - 20~30%
    └── 모델 평가에 사용
```

## 선형 회귀

### 기본 개념

선형 회귀는 데이터를 가장 잘 설명하는 직선을 찾는 문제입니다.

```
y = Wx + b

W: 가중치 (Weight) - 직선의 기울기
b: 바이어스 (Bias) - 직선의 절편
```

### Scikit-Learn을 사용한 선형 회귀

```python
import matplotlib.pyplot as plt
from sklearn import linear_model

# 모델 생성
reg = linear_model.LinearRegression()

# 학습 데이터 (키와 몸무게)
X = [[174], [152], [138], [128], [186]]  # 키 (cm)
y = [71, 55, 46, 38, 88]                  # 몸무게 (kg)

# 학습
reg.fit(X, y)

# 결과 확인
print("기울기:", reg.coef_)           # [0.82021132]
print("절편:", reg.intercept_)        # -68.02
print("정확도:", reg.score(X, y))     # 0.98

# 예측
print("178cm의 예상 몸무게:", reg.predict([[178]]))  # 약 78kg
```

### 시각화

```python
# 학습 데이터 산포도
plt.scatter(X, y, color='black')

# 예측 직선
y_pred = reg.predict(X)
plt.plot(X, y_pred, color='blue', linewidth=3)

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```

### 실습: 간단한 선형 회귀

```python
import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

# 학습 데이터
X = [[1.0], [2.0], [3.0], [4.0], [5.0]]
y = [1.0, 2.0, 1.6, 3.8, 2.3]

# 학습
reg.fit(X, y)

# 시각화
plt.scatter(X, y, color='black')
y_pred = reg.predict(X)
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()
```

## 신경망 기초

### 신경망의 구조

```
입력층 (Input Layer)
    ↓
은닉층 (Hidden Layer)  ← 이 층이 많으면 "딥러닝"
    ↓
출력층 (Output Layer)
```

### 다층 퍼셉트론 (MLP)

여러 개의 은닉층을 가진 신경망을 **다층 퍼셉트론(Multilayer Perceptron)**이라 합니다.

### 뉴런 모델

각 뉴런은 다음과 같이 동작합니다:

```
입력 → [가중치 곱셈 + 편향 더하기] → 활성화 함수 → 출력
```

### 주요 활성화 함수

1. **시그모이드 (Sigmoid)**
   - 출력: 0~1
   - 용도: 이진 분류

2. **ReLU (Rectified Linear Unit)**
   - 출력: max(0, x)
   - 용도: 은닉층에서 주로 사용

3. **Softmax**
   - 출력: 확률 분포
   - 용도: 다중 클래스 분류

### 학습 알고리즘

**역전파(Backpropagation)**
1. 순방향으로 출력 계산
2. 실제 출력과 목표 출력의 오차 계산
3. 오차를 역방향으로 전파하며 가중치 업데이트

**경사하강법(Gradient Descent)**
- 손실 함수를 최소화하는 방향으로 가중치 조정

## Keras 소개

**Keras**는 Python으로 작성된 고수준 딥러닝 API로, TensorFlow 위에서 실행됩니다.

### 주요 특징
- 쉽고 빠른 프로토타이핑
- 다양한 신경망 구조 지원
- CPU/GPU 모두 지원

### 설치 방법

```bash
# TensorFlow 설치 (Keras 포함)
pip install tensorflow

# 또는 Anaconda 환경에서
conda create -n deep python=3.7
conda activate deep
conda install tensorflow
```

### Keras 모델 구축의 기본 흐름

```python
import tensorflow as tf

# 1. 모델 생성
model = tf.keras.models.Sequential()

# 2. 층 추가
model.add(tf.keras.layers.Dense(units=10, activation='relu', input_shape=(5,)))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# 3. 모델 컴파일
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# 4. 모델 학습
model.fit(X_train, y_train, epochs=100)

# 5. 모델 평가
model.evaluate(X_test, y_test)

# 6. 예측
predictions = model.predict(X_new)
```

## XOR 문제 해결

XOR은 단순 선형 분류로는 해결할 수 없는 고전적인 문제입니다.

### XOR 진리표

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |

### Keras로 XOR 해결

```python
import tensorflow as tf
import numpy as np

# 모델 구축
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=2, input_dim=2, activation='sigmoid'))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# 컴파일
sgd = tf.keras.optimizers.SGD(lr=0.1)
model.compile(loss='mean_squared_error', optimizer=sgd)

# 학습 데이터
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# 학습
model.fit(X, y, batch_size=1, epochs=10000, verbose=0)

# 예측
print(model.predict(X))
# [[0.027]
#  [0.970]
#  [0.970]
#  [0.037]]
```

### OR 문제

```python
# OR 진리표
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])  # OR의 정답

model.fit(X, y, batch_size=1, epochs=10000)
print(model.predict(X))
# [[0.021]
#  [0.986]
#  [0.986]
#  [0.997]]
```

## MNIST 숫자 인식

MNIST는 손글씨 숫자 이미지 데이터셋으로, 기계학습의 "Hello World"입니다.

### 데이터셋 정보
- 학습 데이터: 60,000개
- 테스트 데이터: 10,000개
- 이미지 크기: 28×28 픽셀
- 클래스: 0~9 (10개)

### 전체 코드

```python
import matplotlib.pyplot as plt
import tensorflow as tf

# 1. 데이터 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 데이터 정규화 (0~255 → 0~1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. 입력 이미지 확인
plt.imshow(x_train[0], cmap="Greys")
plt.show()

# 4. 모델 구축
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # 28×28을 784로 평탄화
    tf.keras.layers.Dense(512, activation='relu'),   # 은닉층
    tf.keras.layers.Dropout(0.2),                    # 과적합 방지
    tf.keras.layers.Dense(10, activation='softmax')  # 출력층 (10개 클래스)
])

# 5. 컴파일
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 6. 학습
model.fit(x_train, y_train, epochs=5)

# 7. 평가
model.evaluate(x_test, y_test)
```

### 학습 결과

```
Epoch 1/5
60000/60000 - loss: 0.2205 - acc: 0.9348
Epoch 2/5
60000/60000 - loss: 0.0969 - acc: 0.9700
Epoch 3/5
60000/60000 - loss: 0.0678 - acc: 0.9785
Epoch 4/5
60000/60000 - loss: 0.0529 - acc: 0.9834
Epoch 5/5
60000/60000 - loss: 0.0428 - acc: 0.9859

최종 정확도: 약 98.6%
```

### 층별 설명

```python
# Flatten: 2D 이미지를 1D 벡터로 변환
tf.keras.layers.Flatten(input_shape=(28, 28))
# 28×28 → 784

# Dense: 완전 연결층
tf.keras.layers.Dense(512, activation='relu')
# 784개 입력 → 512개 뉴런

# Dropout: 과적합 방지
tf.keras.layers.Dropout(0.2)
# 20% 뉴런을 무작위로 비활성화

# 출력층
tf.keras.layers.Dense(10, activation='softmax')
# 10개 클래스에 대한 확률 출력
```

## 타이타닉 생존자 예측

실제 데이터를 사용한 이진 분류 문제입니다.

### 1. 라이브러리 및 데이터 로드

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

# 데이터 로드
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# 데이터 확인
print(train.head())
```

### 2. 데이터 시각화

```python
# 성별에 따른 생존율
df = train.groupby('Sex').mean()["Survived"]
df.plot(kind='bar')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.show()
```

### 3. 데이터 정제

```python
# 불필요한 열 제거
train.drop([
    'SibSp', 'Parch', 'Ticket', 'Embarked', 
    'Name', 'Cabin', 'PassengerId', 'Fare', 'Age'
], inplace=True, axis=1)

print(train.head())
#    Survived  Pclass     Sex
# 0         0       3    male
# 1         1       1  female
# 2         1       3  female
```

### 4. 범주형 데이터를 숫자로 변환

```python
# 성별을 숫자로 변환 (male: 1, female: 0)
for ix in train.index:
    if train.loc[ix, 'Sex'] == "male":
        train.loc[ix, 'Sex'] = 1
    else:
        train.loc[ix, 'Sex'] = 0

# 또는 pandas의 map 사용
train['Sex'] = train['Sex'].map({'male': 1, 'female': 0})
```

### 5. 데이터 분리

```python
# 특징과 레이블 분리
target = train['Survived'].values
train = train[['Pclass', 'Sex']].values
```

### 6. 모델 구축 및 학습

```python
# 모델 구축
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 컴파일
model.compile(
    loss='binary_crossentropy',  # 이진 분류
    optimizer='adam',
    metrics=['accuracy']
)

# 학습
model.fit(train, target, epochs=30, batch_size=1, verbose=1)
```

### 7. 결과

```
Epoch 30/30
891/891 - loss: 0.4547 - acc: 0.7789

최종 정확도: 약 78%
```

### 개선 방법

1. **더 많은 특징 사용**
   - Age, Fare 등 추가

2. **결측치 처리**
   - 평균값이나 중간값으로 채우기

3. **특징 공학**
   - 새로운 특징 생성 (가족 크기 등)

4. **모델 튜닝**
   - 층 수, 뉴런 수 조정
   - 학습률, 배치 크기 조정

## 주요 개념 정리

### 손실 함수 (Loss Function)

모델 예측과 실제 값의 차이를 측정

- **MSE (Mean Squared Error)**: 회귀 문제
- **Binary Crossentropy**: 이진 분류
- **Categorical Crossentropy**: 다중 클래스 분류

### 옵티마이저 (Optimizer)

손실을 최소화하는 방법

- **SGD (Stochastic Gradient Descent)**: 기본 경사하강법
- **Adam**: 적응적 학습률 (가장 많이 사용)
- **RMSprop**: RNN에 효과적

### 평가 지표 (Metrics)

- **Accuracy**: 정확도
- **Precision**: 정밀도
- **Recall**: 재현율
- **F1-Score**: 정밀도와 재현율의 조화평균

## 실전 팁

### 과적합(Overfitting) 방지

```python
# 1. Dropout 사용
model.add(tf.keras.layers.Dropout(0.3))

# 2. Early Stopping
from tf.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', patience=5)
model.fit(X, y, validation_split=0.2, callbacks=[early_stop])

# 3. 정규화 (L2 Regularization)
from tf.keras import regularizers
model.add(tf.keras.layers.Dense(64, 
    kernel_regularizer=regularizers.l2(0.01)))
```

### 모델 저장 및 로드

```python
# 모델 저장
model.save('my_model.h5')

# 모델 로드
loaded_model = tf.keras.models.load_model('my_model.h5')
```

### 학습 과정 시각화

```python
history = model.fit(X_train, y_train, epochs=100, 
                    validation_data=(X_val, y_val))

# 손실 그래프
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='validation')
plt.legend()
plt.show()
```

## 참고자료

- [TensorFlow 공식 문서](https://www.tensorflow.org/)
- [Keras 공식 문서](https://keras.io/)
- [Scikit-Learn 공식 문서](https://scikit-learn.org/)
- [MNIST 데이터셋](http://yann.lecun.com/exdb/mnist/)
- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
