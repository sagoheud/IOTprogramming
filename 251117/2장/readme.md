# 파이썬 익스프레스 - 2장 요약

## 📚 변수와 수식

### 학습 목표

- ✅ 변수와 상수를 정의하고 사용할 수 있다
- ✅ 주석의 개념을 이해한다
- ✅ 산술 연산자와 할당 연산자를 이해한다
- ✅ 연산자의 우선순위 개념을 이해한다
- ✅ 사용자로부터 입력을 받고 출력하는 프로그램을 작성할 수 있다
- ✅ 문자열의 기초 연산을 이해한다

---

## 🔤 변수 (Variable)

### 변수란?

컴퓨터의 메모리 공간에 이름을 붙여 값을 저장하는 공간

```python
# 변수 정의하기
x = 100
print(x)  # 100

x = 200
print(x)  # 200
```

### 파이썬의 변수 특징

- **자동 생성**: 변수에 값을 저장하면 자동으로 생성됨
- **참조 방식**: 변수에는 실제 값이 아닌 객체의 참조값(주소)이 저장됨
- **동적 타입**: 변수에 어떤 자료형도 저장 가능 (하지만 권장하지 않음)

```python
radius = 10        # 정수
radius = 10.003    # 실수로 변경 가능
radius = "Unknown" # 문자열로 변경 가능 (비권장)
```

### 변수 이름 규칙

✅ **지켜야 할 규칙**
- 영문자, 숫자, 밑줄(_)로 구성
- 첫 글자는 영문자나 밑줄로 시작 (숫자 불가)
- 대소문자 구분 (x와 X는 다른 변수)
- 중간에 공백 사용 불가

✅ **권장 사항**
- 의미 있는 이름 사용
- 낙타체(camelCase) 또는 스네이크 케이스(snake_case) 사용

```python
# 좋은 예
student_name = "홍길동"
totalPrice = 15000
index_value = 10

# 나쁜 예
# 123abc = 10     # 숫자로 시작 불가
# my name = "홍"  # 공백 사용 불가
# class = 100     # 예약어 사용 불가
```

---

## 📊 자료형 (Data Types)

### 주요 자료형

| 자료형 | 설명 | 예시 |
|--------|------|------|
| **int** | 정수 | `10`, `-5`, `0` |
| **float** | 실수 | `3.14`, `-0.5`, `2.0` |
| **str** | 문자열 | `"Hello"`, `'Python'` |
| **bool** | 논리값 | `True`, `False` |

### 자료형 확인하기

```python
type(12.30)    # <class 'float'>
type("hello")  # <class 'str'>
type(100)      # <class 'int'>
```

### 불변 객체 vs 가변 객체

**불변 객체 (Immutable)**
- 한번 생성되면 변경 불가
- 예: 정수, 실수, 문자열, 튜플

**가변 객체 (Mutable)**
- 생성 후에도 변경 가능
- 예: 리스트, 딕셔너리, 세트

---

## 🔢 산술 연산자

### 기본 연산자

```python
# 사칙연산
print(10 + 3)   # 13 (덧셈)
print(10 - 3)   # 7  (뺄셈)
print(10 * 3)   # 30 (곱셈)
print(10 / 3)   # 3.333... (나눗셈)

# 특수 연산
print(10 // 3)  # 3 (몫)
print(10 % 3)   # 1 (나머지)
print(2 ** 3)   # 8 (지수, 2의 3승)
```

### 실전 예제: 요일 계산

```python
today = 0  # 월요일
print((today + 10) % 7)  # 10일 후 요일: 3 (목요일)
```

---

## 🔄 할당 연산자

### 기본 할당

```python
# 다중 할당
x = y = z = 0

# 동시 할당
x, y, z = 10, 20, 30

# 값 교환
x, y = y, x
```

### 복합 연산자

| 연산자 | 의미 | 예시 |
|--------|------|------|
| `+=` | 더하고 할당 | `x += 2` → `x = x + 2` |
| `-=` | 빼고 할당 | `x -= 2` → `x = x - 2` |
| `*=` | 곱하고 할당 | `x *= 2` → `x = x * 2` |
| `/=` | 나누고 할당 | `x /= 2` → `x = x / 2` |
| `//=` | 몫을 구하고 할당 | `x //= 2` → `x = x // 2` |
| `%=` | 나머지를 구하고 할당 | `x %= 2` → `x = x % 2` |
| `**=` | 거듭제곱하고 할당 | `x **= 2` → `x = x ** 2` |

```python
x = 1000
x += 2   # x = 1002
x -= 2   # x = 1000
x *= 2   # x = 2000
```

---

## 📝 주석 (Comments)

### 주석의 용도

1. 코드 설명
2. 임시로 코드 비활성화

```python
# 이것은 한 줄 주석입니다
x = 100  # 변수에 100 저장

"""
이것은
여러 줄 주석입니다
"""

# 원의 면적을 계산하는 프로그램
radius = 10  # 반지름
area = 3.14 * radius * radius  # 면적 계산
print("면적=", area)
```

---

## 🔤 문자열 (String)

### 문자열 생성

```python
# 큰따옴표 사용
msg = "Hello"

# 작은따옴표 사용
msg = 'Hello'

# 따옴표 혼합 사용
message = "철수가 '안녕'이라고 말했습니다."
message = '철수가 "안녕"이라고 말했습니다.'

# 여러 줄 문자열
poem = """TWINKLE, twinkle, little star,
How I wonder what you are!"""
```

### 문자열 연산

```python
# 문자열 결합
print("Hello " + "World!")  # Hello World!

# 문자열 반복
print("=" * 30)  # ==============================
print("Ha" * 3)  # HaHaHa

# 문자열 인덱싱
s = "Hello World"
print(s[0])   # H
print(s[-1])  # d
print(s[6])   # W
```

### 문자열 함수

```python
name = "Harry Potter"

# 소문자 변환
lower_name = name.lower()  # 'harry potter'

# 대문자 변환
upper_name = name.upper()  # 'HARRY POTTER'

# 문자열 치환
new_name = name.replace("Potter", "Porter")  # 'Harry Porter'

# 문자열 길이
length = len(name)  # 12
```

### 특수 문자

```python
print("말 한마디로\n천냥빚을 갚는다")
# 출력:
# 말 한마디로
# 천냥빚을 갚는다

print("탭\t문자")  # 탭    문자
```

---

## 🔄 타입 변환

### 형변환 함수

```python
# 문자열 → 정수
price = int("100")        # 100

# 문자열 → 실수
pi = float("3.14")        # 3.14

# 숫자 → 문자열
movie = "Terminator" + str(3)  # "Terminator3"

# 반올림
tax = round(925.875, 2)   # 925.88
```

### 숫자와 문자열의 차이

```python
print(100 + 200)        # 300 (숫자 덧셈)
print("100" + "200")    # "100200" (문자열 결합)
```

---

## ⌨️ 입력과 출력

### input() 함수

```python
# 문자열 입력
name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")

# 정수 입력
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
print("합은", x + y)

# 실수 입력
height = float(input("키를 미터 단위로 입력하시오: "))
print("키:", height, "m")
```

### print() 함수

```python
# 기본 출력
print("Hello", "World")  # Hello World

# 여러 값 출력
x = 100
y = 200
print(x, "와", y, "의 합=", x + y)  # 100 와 200 의 합= 300

# f-string 사용 (Python 3.6+)
print(f"{x}와 {y}의 합={x+y}")     # 100와 200의 합=300

# 형식화된 출력
pi = 3.141592
print("%.2f" % pi)  # 3.14
```

---

## 💡 상수 (Constant)

### 상수 정의

변수 이름을 대문자로 작성하여 일반 변수와 구분

```python
PI = 3.14159           # 원주율
TAX_RATE = 0.1         # 세율
MAX_SPEED = 120        # 최대 속도

# 사용 예
radius = 5
area = PI * radius * radius
```

---

## 🔢 연산자 우선순위

### 우선순위표 (높은 순서)

1. `**` (지수)
2. `*`, `/`, `//`, `%` (곱셈, 나눗셈)
3. `+`, `-` (덧셈, 뺄셈)
4. `=` (할당)

### 괄호 사용

```python
print(10 + 20 / 2)    # 20.0
print((10 + 20) / 2)  # 15.0

result = 2 + 3 * 4    # 14 (3*4=12, 2+12=14)
result = (2 + 3) * 4  # 20 (2+3=5, 5*4=20)
```

---

## 📝 실습 예제

### 예제 1: 원의 면적 계산

```python
# 원의 면적 계산
radius = 10
area = 3.14 * radius * radius
print("반지름", radius, "인 원의 면적=", area)
```

### 예제 2: BMI 계산

```python
# BMI 계산 프로그램
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))
bmi = weight / (height ** 2)
print("당신의 BMI=", bmi)
```

### 예제 3: 복리 계산

```python
# 복리 계산
init_money = 24       # 초기 금액
interest = 0.06       # 이자율
years = 382           # 기간

result = init_money * (1 + interest) ** years
print(f"{years}년 후 금액: {result}")
```

### 예제 4: 자동판매기 거스름돈

```python
# 거스름돈 계산
itemPrice = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

# 거스름돈 계산
change = note*1000 + coin500*500 + coin100*100 - itemPrice

# 동전별 개수 계산
nCoin500 = change // 500
change = change % 500

nCoin100 = change // 100
change = change % 100

nCoin10 = change // 10
change = change % 10

nCoin1 = change

print(f"500원={nCoin500} 100원={nCoin100} 10원={nCoin10} 1원={nCoin1}")
```

### 예제 5: 로봇 기자 프로그램

```python
# 로봇 기자 프로그램
stadium = input("경기장은 어디입니까? ")
winner = input("이긴팀은 어디입니까? ")
loser = input("진팀은 어디입니까? ")
vip = input("우수선수는 누구입니까? ")
score = input("스코어는 몇대몇입니까? ")

print("\n" + "="*40)
print(f"오늘 {stadium}에서 야구 경기가 열렸습니다.")
print(f"{winner}과 {loser}은 치열한 공방전을 펼쳤습니다.")
print(f"{vip}이 맹활약을 하였습니다.")
print(f"결국 {winner}가 {loser}를 {score}로 이겼습니다.")
print("="*40)
```

### 예제 6: 터틀 그래픽 - 가변 크기 사각형

```python
import turtle

t = turtle.Turtle()
t.shape("turtle")

# 사용자로부터 크기 입력
size = int(input("사각형의 크기는 얼마로 할까요? "))

# 사각형 그리기
for i in range(4):
    t.forward(size)
    t.right(90)

turtle.mainloop()
turtle.bye()
```

---

## 📋 핵심 요약

| 개념 | 설명 | 예시 |
|------|------|------|
| **변수** | 값을 저장하는 메모리 공간 | `x = 100` |
| **상수** | 변경되지 않는 값 (관례상 대문자) | `PI = 3.14` |
| **자료형** | 데이터의 종류 | `int`, `float`, `str` |
| **산술 연산자** | 수학 계산 | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **할당 연산자** | 값 저장 및 연산 | `=`, `+=`, `-=`, `*=` |
| **문자열** | 텍스트 데이터 | `"Hello"`, `'World'` |
| **입력** | 사용자로부터 데이터 받기 | `input()` |
| **출력** | 화면에 결과 표시 | `print()` |
| **형변환** | 자료형 변환 | `int()`, `float()`, `str()` |
| **주석** | 코드 설명 | `# 주석` |

---

## ✅ 학습 점검

- [ ] 변수의 개념과 사용법 이해
- [ ] 다양한 자료형 이해 (int, float, str)
- [ ] 산술 연산자 사용법 숙지
- [ ] 복합 연산자 활용
- [ ] 연산자 우선순위 이해
- [ ] 문자열 연산 및 함수 사용
- [ ] input()과 print() 함수 활용
- [ ] 타입 변환 방법 이해
- [ ] 주석 작성 방법 습득

---

## 🎯 연습 문제

1. **삼각형 면적 계산**: 밑변과 높이를 입력받아 삼각형 면적 계산
2. **온도 변환**: 섭씨를 화씨로 변환 (F = C × 9/5 + 32)
3. **시간 변환**: 초를 입력받아 시, 분, 초로 변환
4. **환율 계산기**: 원화를 달러로 변환
5. **나이 계산**: 출생년도를 입력받아 현재 나이 계산

---
