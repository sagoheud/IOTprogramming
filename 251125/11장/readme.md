# Python 내장함수, 람다식, 제너레이터, 모듈 정리

## 📌 주요 내장 함수

### 수치 관련
- `abs(x)` - 절대값 반환
- `sum(iterable, start=0)` - 합계 반환
- `max(iterable)` - 최댓값 반환
- `min(iterable)` - 최솟값 반환

### 논리 판단
- `all(iterable)` - 모든 요소가 참이면 True
- `any(iterable)` - 하나라도 참이면 True

### 변환 함수
- `list(iterable)` - 리스트로 변환
- `eval(expression)` - 문자열 수식 실행

### 객체 정보
- `len(object)` - 길이 반환
- `dir(object)` - 객체의 속성/메서드 목록 표시

---

## 🔄 고급 함수

### map()
함수를 모든 요소에 적용
```python
def square(n):
    return n*n

result = list(map(square, [1, 2, 3, 4, 5]))
# [1, 4, 9, 16, 25]
```

### filter()
조건을 만족하는 요소만 추출
```python
def myfilter(x):
    return x > 3

result = list(filter(myfilter, [1, 2, 3, 4, 5, 6]))
# [4, 5, 6]
```

### enumerate()
인덱스와 값을 함께 반환
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

### zip()
여러 자료형을 하나로 묶음
```python
numbers = [1, 2, 3, 4]
slist = ['one', 'two', 'three', 'four']
list(zip(numbers, slist))
# [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
```

---

## 🔍 정렬

### 기본 정렬
```python
sorted([4, 2, 3, 5, 1])  # [1, 2, 3, 4, 5]

myList = [4, 2, 3, 5, 1]
myList.sort()  # 리스트 자체를 변경
```

### key 매개변수 사용
```python
# 튜플 정렬
students = [
    ('홍길동', 3.9, 20160303),
    ('김철수', 3.0, 20160302),
    ('최자영', 4.3, 20160301),
]
sorted(students, key=lambda student: student[2])
```

### 클래스 객체 정렬
```python
class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number
    
    def __repr__(self):
        return repr((self.name, self.grade, self.number))

students = [
    Student('홍길동', 3.9, 20160303),
    Student('김철수', 3.0, 20160302),
    Student('최자영', 4.3, 20160301),
]

# 학번순 정렬
sorted(students, key=lambda student: student.number)

# 내림차순 정렬
sorted(students, key=lambda student: student.number, reverse=True)
```

---

## ⚡ 람다식 (Lambda)

### 기본 구조
```python
lambda 매개변수: 표현식
```

### 일반 함수와 비교
```python
# 람다식
f = lambda x, y: x + y
print(f(10, 20))  # 30

# 일반 함수
def get_sum(x, y):
    return x + y
print(get_sum(10, 20))  # 30
```

### map()과 함께 사용
```python
list_a = [1, 2, 3, 4, 5]
result = map(lambda x: 2*x, list_a)
print(list(result))  # [2, 4, 6, 8, 10]
```

### filter()와 함께 사용
```python
list_a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, list_a)
print(list(result))  # [2, 4, 6]
```

### sorted()와 함께 사용
```python
data = [(3, 100), (1, 200), (7, 300), (6, 400)]
sorted(data, key=lambda item: item[0])
# [(1, 200), (3, 100), (6, 400), (7, 300)]
```

### reduce()와 함께 사용
```python
import functools
result = functools.reduce(lambda x, y: x+y, [1, 2, 3, 4])
print(result)  # 10
```

---

## 🔁 이터레이터 (Iterator)

### 이터레이터 클래스 만들기
```python
class MyCounter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# 사용
c = MyCounter(1, 10)
for i in c:
    print(i, end=' ')  # 1 2 3 4 5 6 7 8 9 10
```

---

## 🎯 제너레이터 (Generator)

### 기본 사용
```python
def myGenerator():
    yield 'first'
    yield 'second'
    yield 'third'

for word in myGenerator():
    print(word)
# first
# second
# third
```

### 피보나치 제너레이터
```python
class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue
    
    def __iter__(self):
        return self
    
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b
        self.b = n
        return n

for i in FibIterator():
    print(i, end=" ")  # 1 1 2 3 5 8 13 21 34
```

---

## 🔧 연산자 오버로딩

### Point 클래스 예제
```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Point(4, 6)
```

---

## 📦 모듈 (Module)

### 모듈 작성
```python
# fibo.py
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
```

### 모듈 사용
```python
# 방법 1
import fibo
fibo.fib(1000)

# 방법 2
from fibo import fib
fib(1000)

# 방법 3 (모든 함수 import)
from fibo import *
fib(500)

# 방법 4 (별칭 사용)
import fibo as fb
fb.fib(1000)
```

---

## 🛠️ 유용한 모듈

### random 모듈
```python
import random

# 랜덤 정수
random.randint(1, 6)  # 1~6 사이 정수

# 랜덤 실수
random.random() * 100  # 0~100 사이 실수

# 리스트에서 랜덤 선택
myList = ["red", "green", "blue"]
random.choice(myList)

# 리스트 섞기
random.shuffle(myList)

# 범위 내 랜덤 (step 포함)
random.randrange(0, 101, 3)  # 0~100, 3씩 증가
```

### copy 모듈
```python
import copy

colors = ["red", "blue", "green"]
clone = copy.deepcopy(colors)  # 깊은 복사
clone[0] = "white"

print(colors)  # ['red', 'blue', 'green']
print(clone)   # ['white', 'blue', 'green']
```

### time 모듈
```python
import time

start = time.time()
# 실행할 코드
end = time.time()
print(end - start)  # 실행 시간
```

### sys 모듈
```python
import sys

sys.prefix      # 파이썬 설치 경로
sys.executable  # 파이썬 실행 파일 경로
```

### calendar 모듈
```python
import calendar

cal = calendar.month(2016, 8)
print(cal)  # 2016년 8월 달력 출력
```

### keyword 모듈
```python
import keyword

keyword.iskeyword('for')  # True
keyword.kwlist  # 예약어 목록
```

---

## 💡 핵심 요약

1. **내장 함수**: len(), max(), sum(), all(), any() 등 자주 사용
2. **람다식**: 간단한 일회용 함수에 사용, `lambda 매개변수: 표현식`
3. **map/filter**: 리스트 변환과 필터링에 람다식과 함께 사용
4. **정렬**: `sorted()`의 `key` 매개변수로 정렬 기준 지정
5. **이터레이터**: `__iter__`와 `__next__` 메서드 구현
6. **제너레이터**: `yield` 키워드로 간단하게 이터레이터 생성
7. **모듈**: 코드 재사용을 위해 함수를 파일로 분리
