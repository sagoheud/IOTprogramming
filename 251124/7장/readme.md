# 파이썬 자료구조 II - 튜플, 세트, 딕셔너리, 문자열

## 📚 학습 목표

- 튜플을 이해하고 사용할 수 있다
- 세트를 이해하고 활용할 수 있다
- 딕셔너리를 이해하고 활용할 수 있다
- 문자열의 각종 연산을 이해하고 활용할 수 있다

## 📦 시퀀스(Sequence)

시퀀스는 요소들이 순서를 가지고 저장되는 자료구조입니다.

### 시퀀스의 특징
- 요소(element)로 구성
- 요소 간에는 순서가 있음
- 요소들은 번호가 붙여져 있음
- 인덱싱, 슬라이싱, 덧셈, 곱셈 연산 지원
- 내장함수 사용 가능: `len()`, `max()`, `min()`

### 내장 시퀀스 타입
- `str` (문자열)
- `bytes`, `bytearray`
- `list` (리스트)
- `tuple` (튜플)
- `range`

---

## 🔒 튜플 (Tuple)

튜플은 **변경이 불가능한(immutable)** 리스트입니다.

### 튜플 생성

```python
# 기본 생성
fruits = ("apple", "banana", "grape")
numbers = (1, 2, 3, 4, 5)

# 빈 튜플
empty = ()

# 요소가 하나인 튜플 (쉼표 필수!)
single_tuple = ("apple",)  # 올바름
no_tuple = ("apple")       # 문자열이 됨 (튜플 아님)
```

### 튜플 접근 및 특징

```python
fruits = ("apple", "banana", "grape")
print(fruits[1])   # banana

# 변경 불가능!
fruits[1] = "pear"  # TypeError 발생!
```

### 튜플 ↔ 리스트 변환

```python
# 리스트 → 튜플
myList = [1, 2, 3, 4]
myTuple = tuple(myList)  # (1, 2, 3, 4)

# 튜플 → 리스트
myTuple = (1, 2, 3, 4)
myList = list(myTuple)   # [1, 2, 3, 4]
```

### 튜플 연산

```python
# 튜플 합치기
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi")
# ("apple", "banana", "grape", "pear", "kiwi")

# 리스트에 튜플 추가
numbers = [10, 20, 30]
numbers += (40, 50)
# [10, 20, 30, 40, 50]
```

### 튜플 패킹과 언패킹

```python
# 패킹 (여러 값을 튜플로 묶기)
person = "Kim", 25, "Seoul"

# 언패킹 (튜플의 값을 여러 변수에 할당)
name, age, city = person

# 값 교환
n1, n2 = 10, 90
n1, n2 = n2, n1  # n1=90, n2=10

# 함수에서 여러 값 반환
def get_info():
    return "Kim", 25, "Seoul"

name, age, city = get_info()
```

### enumerate() 함수

인덱스와 값을 동시에 얻을 수 있습니다.

```python
fruits = ["apple", "banana", "grape"]
for index, value in enumerate(fruits):
    print(index, value)

# 출력:
# 0 apple
# 1 banana
# 2 grape
```

### 튜플의 장점
1. **성능**: 리스트보다 빠름
2. **안전성**: 데이터 보호 (변경 불가)
3. **딕셔너리 키**: 튜플은 딕셔너리의 키로 사용 가능
4. **언패킹**: 여러 값을 한 번에 반환

---

## 🎲 세트 (Set)

세트는 **고유한 값들만 저장**하는 자료구조로, **순서가 없습니다**.

### 세트 생성

```python
# 기본 생성
fruits = {"apple", "banana", "grape"}

# 빈 세트 (주의: {}는 딕셔너리!)
empty_set = set()

# 리스트로부터 세트 생성 (중복 제거)
numbers = set([1, 2, 3, 1, 2, 3])
print(numbers)  # {1, 2, 3}

# 문자열로부터 세트 생성
letters = set("abc")  # {'a', 'b', 'c'}
```

### 세트 연산

```python
fruits = {"apple", "banana", "grape"}

# 길이
size = len(fruits)  # 3

# 멤버십 테스트
if "apple" in fruits:
    print("집합 안에 apple이 있습니다.")

# 반복 (순서는 보장되지 않음)
for x in fruits:
    print(x, end=" ")

# 정렬된 순서로 반복
for x in sorted(fruits):
    print(x, end=" ")
```

### 세트에 요소 추가/삭제

```python
fruits = {"apple", "banana"}

# 요소 추가
fruits.add("grape")

# 요소 삭제
fruits.remove("banana")      # 없으면 예외 발생
fruits.discard("banana")     # 없어도 예외 발생 안 함

# 전체 삭제
fruits.clear()
```

### 세트 함축

```python
# 짝수의 제곱만
squares = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}
```

### 집합 연산

```python
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}

# 부분집합 확인
A.issubset(B)     # True
A <= B            # True

# 상위집합 확인
B.issuperset(A)   # True
B >= A            # True

# 동등 비교
A == B            # False
A != B            # True
```

### 합집합 (Union)

```python
A = {"apple", "banana"}
B = {"grape", "kiwi"}

# 방법 1: | 연산자
result = A | B

# 방법 2: union() 메소드
result = A.union(B)

# {'apple', 'banana', 'grape', 'kiwi'}
```

### 교집합 (Intersection)

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# 방법 1: & 연산자
result = A & B

# 방법 2: intersection() 메소드
result = A.intersection(B)

# {3, 4, 5}
```

### 차집합 (Difference)

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# 방법 1: - 연산자
result = A - B  # {1, 2}

# 방법 2: difference() 메소드
result = A.difference(B)  # {1, 2}
```

### 세트 활용 예제

```python
# 중복 제거
list1 = [1, 2, 3, 4, 5, 1, 2, 4]
unique_count = len(set(list1))  # 5

# 공통 요소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)  # {3, 4, 5}
```

---

## 📖 딕셔너리 (Dictionary)

딕셔너리는 **키(key)와 값(value)의 쌍**으로 데이터를 저장합니다.

### 딕셔너리 생성

```python
# 기본 생성
capitals = {
    "Korea": "Seoul",
    "USA": "Washington",
    "UK": "London"
}

# 빈 딕셔너리
empty_dict = {}
# 또는
empty_dict = dict()
```

### 항목 접근

```python
capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}

# 방법 1: [] 연산자 (키가 없으면 오류)
print(capitals["Korea"])  # Seoul
print(capitals["France"]) # KeyError 발생!

# 방법 2: get() 메소드 (안전)
print(capitals.get("France", "해당 키가 없습니다."))
# "해당 키가 없습니다."
```

### 항목 추가/수정

```python
capitals = {}
capitals["Korea"] = "Seoul"
capitals["USA"] = "Washington"
capitals["UK"] = "London"

# 기존 키에 할당하면 값 수정
capitals["Korea"] = "서울"
```

### 항목 삭제

```python
capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}

# pop() 메소드 (키가 없으면 오류)
city = capitals.pop("UK")

# 안전한 삭제
if "UK" in capitals:
    capitals.pop("UK")

# del 키워드
del capitals["USA"]

# 전체 삭제
capitals.clear()
```

### 항목 방문

```python
capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}

# 방법 1: 키만 반복
for key in capitals:
    print(key, ":", capitals[key])

# 방법 2: items() 사용 (권장)
for key, value in capitals.items():
    print(key, ":", value)

# 출력:
# Korea : Seoul
# USA : Washington
# UK : London
```

### 딕셔너리 메소드

```python
capitals = {"Korea": "Seoul", "USA": "Washington", "UK": "London"}

# 모든 키
print(capitals.keys())
# dict_keys(['Korea', 'USA', 'UK'])

# 모든 값
print(capitals.values())
# dict_values(['Seoul', 'Washington', 'London'])

# 정렬된 키로 반복
for key in sorted(capitals.keys()):
    print(key, end=" ")
# Korea UK USA
```

### 딕셔너리 함축

```python
# 짝수만 제곱
values = [1, 2, 3, 4, 5, 6]
dic = {x: x**2 for x in values if x % 2 == 0}
# {2: 4, 4: 16, 6: 36}

# 숫자를 문자열로
dic = {i: str(i) for i in [1, 2, 3, 4, 5]}
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}

# 과일 이름 길이
fruits = ["apple", "orange", "banana"]
dic = {f: len(f) for f in fruits}
# {'apple': 5, 'orange': 6, 'banana': 6}
```

---

## 🔤 문자열 (String)

문자열도 시퀀스 자료구조입니다.

### 문자 코드 변환

```python
# 문자 → 코드
ord("a")    # 97
ord("가")   # 44032

# 코드 → 문자
chr(97)     # 'a'
chr(44032)  # '가'
```

### 문자열 인덱싱

```python
s = "Monty Python"
print(s[0])   # 'M'
print(s[-1])  # 'n'
```

### 문자열 슬라이싱

```python
s = "Monty Python"

# 기본 슬라이싱
print(s[6:10])  # 'Pyth'
print(s[:2])    # 'Mo'
print(s[4:])    # 'y Python'
print(s[:])     # 'Monty Python' (전체 복사)

# 활용 예제
message = "see you at noon"
low = message[:5]   # 'see y'
high = message[5:]  # 'ou at noon'

reg = "980326"
print(reg[0:2] + "년")  # '98년'
print(reg[2:4] + "월")  # '03월'
print(reg[4:6] + "일")  # '26일'
```

### 문자열 불변성

```python
word = "abcdef"
word[0] = "A"  # TypeError! 문자열은 변경 불가능

# 새 문자열 생성
word = "A" + word[1:]  # 'Abcdef'
```

### 문자열 비교

```python
a = input("문자열을 입력하시오: ")
b = input("문자열을 입력하시오: ")

if a < b:
    print(a, "가 앞에 있음")
else:
    print(b, "가 앞에 있음")

# 입력: apple, orange
# 출력: apple 가 앞에 있음
```

### 문자열 포매팅

```python
x = 25
y = 98
prod = x * y

# 방법 1: 여러 인자
print(x, "과", y, "의 곱은", prod)
# 25 과 98 의 곱은 2450

# 방법 2: f-문자열 (권장)
print(f"{x}과 {y}의 곱은 {prod}")
# 25과 98의 곱은 2450
```

### 대소문자 변환

```python
s = "i am a student."
s.capitalize()  # 'I am a student.'

s = "Breakfast At Tiffany"
s.lower()       # 'breakfast at tiffany'
s.upper()       # 'BREAKFAST AT TIFFANY'
```

### 찾기 및 바꾸기

```python
# 끝 문자 확인
s = "test.py"
s.endswith(".py")   # True
s.startswith("test") # True

# 문자열 교체
s = "www.naver.com"
s.replace("com", "co.kr")  # 'www.naver.co.kr'

# 찾기
s = "www.naver.co.kr"
s.find(".kr")     # 12 (위치 반환)
s.find(".jp")     # -1 (없으면 -1)

s = "Let it be, let it be, let it be"
s.rfind("let")    # 22 (오른쪽부터 찾기)

# 개수 세기
s = "www.naver.co.kr"
s.count(".")      # 3
```

### 문자 분류

```python
"ABCabc".isalpha()  # True (알파벳?)
"123".isdigit()     # True (숫자?)
"abc".islower()     # True (소문자?)
"ABC".isupper()     # True (대문자?)
"abc123".isalnum()  # True (알파벳+숫자?)
```

### 공백 제거

```python
s = "  Hello, World!  "
s.strip()   # 'Hello, World!' (양쪽)
s.lstrip()  # 'Hello, World!  ' (왼쪽)
s.rstrip()  # '  Hello, World!' (오른쪽)

# 특정 문자 제거
s = "########this is example#####"
s.strip("#")   # 'this is example'
s.lstrip("#")  # 'this is example#####'
s.rstrip("#")  # '########this is example'
```

### 문자열 분해 (split)

```python
# 공백으로 분리
s = "Welcome to Python"
s.split()  # ['Welcome', 'to', 'Python']

# 구분자 지정
s = "Hello, World!"
s.split(",")   # ['Hello', ' World!']
s.split(", ")  # ['Hello', 'World!']

# 문자 단위 분리
list("Hello")  # ['H', 'e', 'l', 'l', 'o']
```

### 문자열 결합 (join)

```python
# 리스트를 문자열로 결합
",".join(["apple", "grape", "banana"])
# 'apple,grape,banana'

# 전화번호 변환
"-".join("010.1234.5678".split("."))
# '010-1234-5678'
```

---

## 📊 자료구조 비교표

| 특성 | 리스트 | 튜플 | 세트 | 딕셔너리 |
|------|--------|------|------|----------|
| 생성 | `[]` | `()` | `set()` | `{}` |
| 순서 | O | O | X | X (3.7+부터 순서 유지) |
| 중복 | O | O | X | 키 중복 X |
| 변경 가능 | O | X | O | O |
| 인덱싱 | O | O | X | 키로 접근 |
| 용도 | 순서가 있는 데이터 | 불변 데이터 | 고유값 관리 | 키-값 매핑 |

## 🔧 주요 메소드 정리

### 튜플 메소드
| 메소드 | 설명 |
|--------|------|
| `count(x)` | x의 개수 반환 |
| `index(x)` | x의 인덱스 반환 |

### 세트 메소드
| 메소드 | 설명 |
|--------|------|
| `add(x)` | 요소 추가 |
| `remove(x)` | 요소 제거 (없으면 오류) |
| `discard(x)` | 요소 제거 (없어도 오류 없음) |
| `clear()` | 모든 요소 제거 |
| `union()` | 합집합 |
| `intersection()` | 교집합 |
| `difference()` | 차집합 |

### 딕셔너리 메소드
| 메소드 | 설명 |
|--------|------|
| `get(key, default)` | 안전하게 값 가져오기 |
| `pop(key)` | 항목 제거 및 값 반환 |
| `keys()` | 모든 키 반환 |
| `values()` | 모든 값 반환 |
| `items()` | 키-값 쌍 반환 |
| `clear()` | 모든 항목 제거 |

### 문자열 메소드
| 메소드 | 설명 |
|--------|------|
| `upper()` | 대문자 변환 |
| `lower()` | 소문자 변환 |
| `capitalize()` | 첫 글자만 대문자 |
| `strip()` | 공백 제거 |
| `split()` | 문자열 분리 |
| `join()` | 문자열 결합 |
| `replace(old, new)` | 문자열 교체 |
| `find(sub)` | 부분 문자열 찾기 |
| `startswith()` | 시작 문자 확인 |
| `endswith()` | 끝 문자 확인 |

## ⚠️ 주의사항

1. **튜플**: 요소가 하나일 때 쉼표 필수 `(item,)`
2. **세트**: 빈 세트는 `set()`, `{}`는 빈 딕셔너리
3. **딕셔너리**: 없는 키 접근 시 `get()` 메소드 사용 권장
4. **문자열**: 불변 객체이므로 수정 시 새 문자열 생성

## 📚 참고 자료

- [Python 공식 문서 - 튜플](https://docs.python.org/ko/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python 공식 문서 - 세트](https://docs.python.org/ko/3/tutorial/datastructures.html#sets)
- [Python 공식 문서 - 딕셔너리](https://docs.python.org/ko/3/tutorial/datastructures.html#dictionaries)
- [Python 공식 문서 - 문자열](https://docs.python.org/ko/3/library/stdtypes.html#text-sequence-type-str)

---

**학습 완료 체크리스트**
- [ ] 튜플의 불변성 이해
- [ ] 세트의 집합 연산 활용
- [ ] 딕셔너리 키-값 관리
- [ ] 문자열 메소드 활용
- [ ] 자료구조 함축 작성
- [ ] 실습 예제 완료
