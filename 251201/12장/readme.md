# 파이썬 상속 (Inheritance)

## 📚 학습 목표
- 부모 클래스를 상속받아서 자식 클래스 정의하기
- 부모 클래스의 메소드를 자식 클래스에서 재정의하기
- Object 클래스 이해하기
- 메소드 오버라이딩 사용하기
- 클래스 간의 관계 파악하기

---

## 🎯 상속이란?

**상속(Inheritance)**은 기존에 존재하는 클래스로부터 코드와 데이터를 이어받고 자신이 필요한 기능을 추가하는 기법입니다.

### 상속의 장점
- 코드 재사용성 증가
- 중복 코드 제거
- 유지보수 용이
- 계층적 클래스 구조 구현

### is-a 관계
상속은 클래스 간의 "is-a" 관계를 생성합니다.
- 푸들은 강아지이다 (Poodle is a Dog)
- 자동차는 차량이다 (Car is a Vehicle)
- 원은 도형이다 (Circle is a Shape)

---

## 🔧 상속 구현하기

### 기본 문법

```python
class 부모클래스:
    # 부모 클래스 내용
    pass

class 자식클래스(부모클래스):
    # 자식 클래스 내용
    pass
```

### 예제: Car와 ElectricCar

```python
# 부모 클래스: 일반 자동차
class Car:
    def __init__(self, make, model, color, price):
        self.make = make      # 메이커
        self.model = model    # 모델
        self.color = color    # 색상
        self.price = price    # 가격
    
    def setMake(self, make):
        self.make = make
    
    def getMake(self):
        return self.make
    
    def getDesc(self):
        return f"차량 =({self.make},{self.model},{self.color},{self.price})"

# 자식 클래스: 전기 자동차
class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)  # 부모 생성자 호출
        self.batterySize = batterySize               # 추가 속성
    
    def setBatterySize(self, batterySize):
        self.batterySize = batterySize
    
    def getBatterySize(self):
        return self.batterySize

# 사용 예
myCar = ElectricCar("Tesla", "Model S", "white", 10000, 60)
print(myCar.getDesc())
# 출력: 차량 =(Tesla,Model S,white,10000)
```

---

## 🏗️ super()와 생성자

### super() 함수
`super()`는 부모 클래스의 메소드를 호출할 때 사용합니다.

```python
class Animal:
    def __init__(self, age=0):
        self.age = age
    
    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self, age=0, name=""):
        super().__init__(age)  # 부모 생성자 호출 (중요!)
        self.name = name

d = Dog(5, "멍멍이")
print(d.age)   # 5
print(d.name)  # 멍멍이
```

### ⚠️ 주의사항
부모 클래스의 생성자를 호출하지 않으면 부모 클래스의 속성이 초기화되지 않습니다!

```python
class Dog(Animal):
    def __init__(self, age=0, name=""):
        # super().__init__(age)  # 이 줄이 없으면
        self.name = name

d = Dog()
print(d.age)  # AttributeError 발생!
```

---

## 🔒 Private 멤버와 상속

`__` (더블 언더스코어)로 시작하는 private 멤버는 자식 클래스에서 직접 접근할 수 없습니다.

```python
class Parent:
    def __init__(self):
        self.__money = 100  # private 멤버

class Child(Parent):
    def __init__(self):
        super().__init__()

obj = Child()
# print(obj.__money)  # AttributeError 발생!
```

---

## 🎭 메소드 오버라이딩 (Method Overriding)

자식 클래스에서 부모 클래스의 메소드를 재정의하는 것을 **메소드 오버라이딩**이라고 합니다.

### 기본 예제

```python
import math

class Shape:
    def __init__(self):
        pass
    
    def draw(self):
        print("draw()가 호출됨")
    
    def get_area(self):
        print("get_area()가 호출됨")

class Circle(Shape):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius
    
    def draw(self):  # 오버라이딩
        print("원을 그립니다.")
    
    def get_area(self):  # 오버라이딩
        return math.pi * self.radius ** 2

c = Circle(10)
c.draw()              # 원을 그립니다.
print("원의 면적:", c.get_area())  # 원의 면적: 314.159...
```

### 부모 메소드 호출하기

```python
class Circle(Shape):
    def draw(self):
        super().draw()  # 부모 클래스의 draw() 호출
        print("원을 그립니다.")

c = Circle(10)
c.draw()
# 출력:
# draw()가 호출됨
# 원을 그립니다.
```

---

---

## 🔍 타입 확인

### type() 함수

```python
class Animal:
    pass

class Dog(Animal):
    pass

x = Animal()
y = Dog()

print(type(x))  # <class '__main__.Animal'>
print(type(y))  # <class '__main__.Dog'>
```

### isinstance() 함수

```python
x = Animal()
y = Dog()

print(isinstance(x, Animal))  # True
print(isinstance(y, Animal))  # True (Dog는 Animal의 자식)
print(isinstance(x, Dog))     # False
```

---

## 🌳 다중 상속

파이썬은 여러 부모 클래스로부터 상속받을 수 있습니다.

```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```

### 다중 상속 예제

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name, self.age)

class Student:
    def __init__(self, id):
        self.id = id
    
    def getId(self):
        return self.id

class CollegeStudent(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)

obj = CollegeStudent('Kim', 22, '100036')
obj.show()         # Kim 22
print(obj.getId()) # 100036
```

---

## 🎨 다형성 (Polymorphism)

**다형성**은 "많은(poly) + 모양(morph)"의 의미로, 하나의 인터페이스로 다양한 타입을 처리하는 것을 의미합니다.

### 상속과 다형성

```python
class Shape:
    def __init__(self, name):
        self.name = name
    
    def getArea(self):
        raise NotImplementedError("이것은 추상메소드입니다.")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def getArea(self):
        return 3.141592 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height

# 다형성 활용
shapeList = [Circle("c1", 10), Rectangle("r1", 10, 10)]
for s in shapeList:
    print(s.getArea())
# 출력:
# 314.1592
# 100
```

### 내장 함수와 다형성

```python
mylist = [1, 2, 3]
print("리스트의 길이=", len(mylist))        # 3

s = "This is a sentence"
print("문자열의 길이=", len(s))             # 18

d = {'aaa': 1, 'bbb': 2}
print("딕셔너리의 길이=", len(d))           # 2
```

---

## 📦 Object 클래스

모든 파이썬 클래스는 암묵적으로 `object` 클래스를 상속받습니다.

### object 클래스의 주요 메소드

| 메소드 | 설명 |
|--------|------|
| `__init__()` | 생성자 |
| `__str__()` | 문자열 표현 (사용자용) |
| `__repr__()` | 문자열 표현 (개발자용) |
| `__eq__()` | 동등 비교 (==) |
| `__hash__()` | 해시값 반환 |
| `__del__()` | 소멸자 |

### __repr__() 메소드

```python
class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn
    
    def __repr__(self):
        return f"ISBN: {self.__isbn}; TITLE: {self.__title}"

book = Book("The Python Tutorial", "0123456")
print(book)
# 출력: ISBN: 0123456; TITLE: The Python Tutorial
```

### __str__() 메소드

```python
class MyTime:
    def __init__(self, hour, minute, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

time = MyTime(10, 25)
print(time)  # 10:25:00
```

---

## 🔗 클래스 관계

### 1. is-a 관계 (상속)
- 승용차는 차량의 일종이다 (Car is a Vehicle)
- 강아지는 동물의 일종이다 (Dog is an Animal)
- 원은 도형의 일종이다 (Circle is a Shape)

```python
class Animal:
    pass

class Dog(Animal):  # Dog is an Animal
    pass
```

### 2. has-a 관계 (구성/포함)
- 도서관은 책을 가지고 있다 (Library has a Book)
- 거실은 소파를 가지고 있다 (Living room has a Sofa)

```python
class Dog:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None  # Person has a Dog

dog1 = Dog("dog1")
person1 = Person("홍길동")
person1.pet = dog1  # has-a 관계
```

---

---

## 🛠️ 유용한 함수들

### map() 함수

`map()` 함수는 반복 가능한 객체의 각 항목에 주어진 함수를 적용합니다.

```python
def square(n):
    return n * n

mylist = [1, 2, 3, 4, 5]
result = list(map(square, mylist))
print(result)  # [1, 4, 9, 16, 25]

# 람다 함수 사용
result = list(map(lambda x: x * x, mylist))
print(result)  # [1, 4, 9, 16, 25]
```

---

## 📝 핵심 정리

### 상속을 사용해야 하는 경우
- ✅ is-a 관계가 성립할 때
- ✅ 코드 중복을 줄이고 싶을 때
- ✅ 계층적 구조가 필요할 때
- ✅ 다형성을 활용하고 싶을 때

### 상속의 주요 개념
1. **상속**: 부모 클래스의 코드와 데이터를 물려받음
2. **super()**: 부모 클래스의 메소드 호출
3. **오버라이딩**: 부모 메소드를 자식에서 재정의
4. **다형성**: 같은 인터페이스로 다양한 타입 처리
5. **is-a vs has-a**: 상속과 구성의 적절한 선택

### 베스트 프랙티스
- 항상 부모 클래스의 생성자를 호출하기 (`super().__init__()`)
- 메소드 오버라이딩 시 명확한 목적 가지기
- is-a 관계가 아니면 상속 대신 구성 사용하기
- private 멤버(`__`)는 신중하게 사용하기

---

## 🔗 참고 자료

- Python 공식 문서: [Classes](https://docs.python.org/3/tutorial/classes.html)
- Python 상속: [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- Python 다중 상속: [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- 특수 메소드: [Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)

---

## 💡 추가 학습 주제

- 추상 베이스 클래스 (ABC - Abstract Base Class)
- 믹스인 (Mixin) 패턴
- 메소드 해석 순서 (MRO - Method Resolution Order)
- 연산자 오버로딩
- 프로퍼티 (Property) 데코레이터
