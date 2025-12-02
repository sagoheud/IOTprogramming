# NumPy & Matplotlib 가이드

Python 데이터 분석과 시각화를 위한 NumPy와 Matplotlib 라이브러리 사용법 정리

## 목차
- [소개](#소개)
- [Matplotlib 기초](#matplotlib-기초)
- [NumPy 배열](#numpy-배열)
- [데이터 생성](#데이터-생성)
- [난수 생성](#난수-생성)
- [통계 함수](#통계-함수)
- [인덱싱과 슬라이싱](#인덱싱과-슬라이싱)
- [선형대수](#선형대수)

## 소개

**NumPy**는 파이썬에서 행렬 계산을 위한 핵심 라이브러리입니다. 리스트보다 빠른 처리 속도로 인공지능과 데이터 과학에서 널리 사용됩니다.

**Matplotlib**은 데이터 시각화를 위한 그래프 라이브러리로, MATLAB의 무료 오픈소스 대안입니다.

## Matplotlib 기초

### 기본 선 그래프

```python
import matplotlib.pyplot as plt

# 단순 그래프
plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4])
plt.show()

# X, Y 좌표 지정
X = [1, 2, 3, 4, 5, 6, 7]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
plt.plot(X, Y)
plt.show()
```

### 레이블과 제목 추가

```python
X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

plt.plot(X, Y)
plt.xlabel("day")
plt.ylabel("temperature")
plt.title("Weekly Temperature")
plt.show()
```

### 다중 그래프

```python
X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

plt.plot(X, Y1, label="Seoul")
plt.plot(X, Y2, label="Busan")
plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(loc="upper left")
plt.title("Temperatures of Cities")
plt.show()
```

### 막대 그래프

```python
X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

plt.bar(X, Y)
plt.show()
```

### 3D 그래프

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

axis = plt.axes(projection='3d')

Z = np.linspace(0, 1, 100)
X = Z * np.sin(30 * Z)
Y = Z * np.cos(30 * Z)

axis.plot3D(X, Y, Z)
plt.show()
```

## NumPy 배열

### 배열 생성

```python
import numpy as np

# 리스트에서 배열 생성
ftemp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]
F = np.array(ftemp)
print(F)  # array([63, 73, 80, 86, 84, 78, 66, 54, 45, 63])

# 브로드캐스팅: 모든 요소에 연산 적용
celsius = (F - 32) * 5 / 9
```

### 2차원 배열

```python
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b[0][2])  # 3
```

### 배열 연산

```python
A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])
result = A + B  # array([6, 8, 10, 12])

# 비교 연산
a = np.array([0, 9, 21, 3])
print(a < 10)  # array([True, True, False, True])
```

## 데이터 생성

### arange() - 범위 생성

```python
A = np.arange(1, 10, 2)  # 1부터 10 미만까지 2씩 증가
print(A)  # array([1, 3, 5, 7, 9])
```

### linspace() - 균등 분할

```python
A = np.linspace(0, 10, 100)  # 0부터 10까지 100개로 균등 분할
```

## 난수 생성

### 균일 분포 (0~1)

```python
np.random.seed(100)  # 시드 설정
np.random.rand(5)  # 1차원 배열
np.random.rand(5, 3)  # 2차원 배열
```

### 정규 분포

```python
# 평균 0, 표준편차 1
np.random.randn(5)

# 평균과 표준편차 지정
m, sigma = 10, 2
data = m + sigma * np.random.randn(5)

# normal() 함수 사용
mu, sigma = 0, 0.1
np.random.normal(mu, sigma, 5)
```

### 잡음이 포함된 데이터

```python
import numpy as np
import matplotlib.pyplot as plt

pure = np.linspace(1, 10, 100)
noise = np.random.normal(0, 1, 100)
signal = pure + noise

plt.plot(signal)
plt.show()
```

## 통계 함수

```python
scores = np.array([[99, 93, 60], [98, 82, 93],
                   [93, 65, 81], [78, 82, 81]])

# 기본 통계
scores.sum()      # 전체 합
scores.min()      # 최솟값
scores.max()      # 최댓값
scores.mean()     # 평균
scores.std()      # 표준편차
scores.var()      # 분산

# 축 단위 계산 (axis=0: 열, axis=1: 행)
scores.mean(axis=0)  # 각 열의 평균
```

### 히스토그램

```python
import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.normal(size=10000)
plt.hist(numbers)
plt.xlabel("value")
plt.ylabel("freq")
plt.show()
```

## 인덱싱과 슬라이싱

### 기본 슬라이싱

```python
grades = np.array([88, 72, 93, 94])
grades[1:3]  # array([72, 93])
grades[:2]   # array([88, 72])
```

### 논리적 인덱싱

```python
ages = np.array([18, 19, 25, 30, 28])
y = ages > 20
print(y)  # array([False, False, True, True, True])

# 조건에 맞는 요소만 추출
ages[ages > 20]  # array([25, 30, 28])
```

### 2차원 배열 슬라이싱

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a[0:2, 1:3]  # array([[2, 3], [5, 6]])

# 논리적 인덱싱
a[a > 5]  # array([6, 7, 8, 9])
```

## 선형대수

### 전치 행렬

```python
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.transpose()  # 또는 x.T
```

### 역행렬

```python
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
np.dot(x, y)  # 단위행렬 확인
```

### 선형방정식 풀이

```python
# 3*x0 + x1 = 9
# x0 + 2*x1 = 8
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
print(x)  # array([2., 3.])
```

## 라이선스

이 문서는 교육 목적으로 작성되었습니다.

## 참고자료

- [NumPy 공식 문서](https://numpy.org/doc/)
- [Matplotlib 공식 문서](https://matplotlib.org/)
