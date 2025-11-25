# Python 객체와 클래스 (Chapter 8)

## 📚 학습 목표
- 객체지향 프로그래밍의 기본 개념 이해
- 객체와 클래스의 관계 파악
- 객체를 활용한 프로그램 작성

## 🎯 핵심 개념

### 객체 지향 프로그래밍(OOP)
서로 관련 있는 데이터와 함수를 묶어서 **객체(object)**로 만들고, 이들 객체들이 모여서 하나의 프로그램을 구성하는 방식

#### 절차 지향 vs 객체 지향
- **절차 지향**: 프로시저(함수) 기반 프로그래밍
- **객체 지향**: 데이터와 함수를 하나로 묶어서 생각하는 방법

### 객체(Object)
- **속성(Attribute)**: 객체가 가진 데이터 (예: 자동차의 색상, 모델, 가격)
- **동작(Action)**: 객체가 수행하는 행위 (예: 주행, 방향 전환, 정지)

### 클래스(Class)
객체를 만들기 위한 설계도 또는 템플릿
- 클래스로부터 만들어진 객체를 **인스턴스(Instance)**라고 함
- 파이썬에서는 모든 것이 객체! (정수, 문자열, 리스트 등)

## 💻 클래스 작성 기본 문법

### 기본 구조
```python
class ClassName:
    def __init__(self, parameter):
        self.attribute = parameter
    
    def method(self):
        # 메소드 구현
        pass
```

### 생성자 (`__init__`)
객체 생성 시 자동으로 호출되며, 인스턴스 변수를 초기화

```python
class Counter:
    def __init__(self, initValue=0):
        self.count = initValue
    
    def increment(self):
        self.count += 1

a = Counter(100)  # 초기값 100
b = Counter()     # 초기값 0 (기본값)
```

## 🔐 정보 은닉(Information Hiding)

### Private 변수
변수명 앞에 `__`(언더스코어 2개)를 붙여 외부 접근 제한

```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # private 변수
        self.__age = age    # private 변수
```

### 접근자와 설정자
- **Getter**: 값을 읽는 메소드
- **Setter**: 값을 설정하는 메소드

```python
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
```

## 📊 변수의 종류

### 인스턴스 변수 vs 클래스 변수

```python
class Television:
    serialNumber = 0  # 클래스 변수 (모든 객체가 공유)
    
    def __init__(self, channel):
        self.channel = channel  # 인스턴스 변수 (각 객체마다 고유)
        Television.serialNumber += 1
```

## 🔧 특수 메소드(Special Methods)

연산자 오버로딩을 위한 메소드

| 메소드 | 연산자 | 설명 |
|--------|--------|------|
| `__add__` | + | 덧셈 |
| `__sub__` | - | 뺄셈 |
| `__mul__` | * | 곱셈 |
| `__eq__` | == | 동등 비교 |
| `__str__` | str() | 문자열 변환 |

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
```

## 🔍 객체 참조

### 참조의 이해
- 파이썬에서 변수는 객체의 메모리 주소를 저장
- 여러 변수가 같은 객체를 참조할 수 있음

```python
t = Television(11, 10, True)
s = t  # s와 t는 같은 객체를 참조

if s is t:
    print("동일한 객체를 참조합니다")
```

### None 참조
```python
myTV = None
if myTV is None:
    print("현재 TV가 없습니다")
```

## ✨ 주요 개념 정리

1. **캡슐화(Encapsulation)**: 공용 인터페이스만 제공하고 구현 세부사항을 감춤
2. **self**: 메소드 내에서 현재 객체를 참조하는 매개변수
3. **클래스 변수**: 모든 인스턴스가 공유하는 변수
4. **인스턴스 변수**: 각 객체마다 고유한 변수

---

## 📌 체크리스트
- [ ] 클래스와 객체의 차이 이해
- [ ] 생성자 `__init__` 활용
- [ ] 정보 은닉과 getter/setter 구현
- [ ] 클래스 변수와 인스턴스 변수 구분
- [ ] 특수 메소드를 활용한 연산자 오버로딩
