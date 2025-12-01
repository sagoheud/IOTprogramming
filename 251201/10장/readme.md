# 파이썬 파일과 예외처리

## 📚 학습 목표
- 텍스트 파일 읽고 쓰기
- 이진 파일 읽고 쓰기
- 정규식 사용 방법
- CSV 파일 처리
- 예외 처리 방법

---

## 📂 파일 처리

### 파일 열기 및 닫기

#### 기본 문법
```python
# 파일 열기
infile = open("파일경로", "모드")

# 파일 닫기
infile.close()
```

#### 파일 모드
| 모드 | 설명 |
|------|------|
| `r` | 읽기 모드 (기본값) |
| `w` | 쓰기 모드 (파일이 있으면 덮어쓰기) |
| `a` | 추가 모드 (파일 끝에 추가) |
| `rb` | 이진 파일 읽기 |
| `wb` | 이진 파일 쓰기 |

#### with 문을 사용한 안전한 파일 처리
```python
with open("test.txt", "w") as f:
    f.write("김영희\n")
    f.write("최자영\n")
# 블록을 빠져나오면 자동으로 파일이 닫힘
```

---

## 📖 텍스트 파일 읽기

### 한 줄씩 읽기
```python
infile = open("input.txt", "r")
line = infile.readline()
while line != "":
    print(line.rstrip())  # 오른쪽 공백 제거
    line = infile.readline()
infile.close()
```

### 전체 파일 읽기
```python
# 전체를 문자열로 읽기
infile = open("input.txt", "r")
s = infile.read()
print(s)
infile.close()

# 전체를 리스트로 읽기
infile = open("input.txt", "r")
lines = infile.readlines()
for line in lines:
    print(line)
infile.close()
```

### for 루프로 읽기
```python
infile = open("scores.txt", "r")
for line in infile:
    print(line.rstrip())
infile.close()
```

### 문자 단위로 읽기
```python
infile = open("input.txt", "r")
ch = infile.read(1)
while ch != "":
    print(ch)
    ch = infile.read(1)
infile.close()
```

---

## ✍️ 텍스트 파일 쓰기

```python
outfile = open("output.txt", "w")
outfile.write("김영희\n")
outfile.write("홍길동\n")
outfile.close()
```

---

## 🔧 문자열 처리 메서드

```python
s = " Hello, World!\n"
s.strip()      # 양쪽 공백 제거: "Hello, World!"
s.lstrip()     # 왼쪽 공백 제거
s.rstrip()     # 오른쪽 공백 제거

# 단어로 분리
line = "All's well that ends well"
word_list = line.split()  # ['All's', 'well', 'that', 'ends', 'well']
```

---

## 📊 CSV 파일 처리

```python
import csv

f = open('weather.csv')
data = csv.reader(f)
header = next(data)  # 헤더 읽기

temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])

print('가장 추웠던 날은', temp, '입니다')
f.close()
```

---

## 💾 이진 파일 처리

### 이진 파일 읽기
```python
infile = open("123.png", "rb")
bytesArray = infile.read(8)  # 8바이트 읽기
byte1 = bytesArray[0]        # 첫 번째 바이트
infile.close()
```

### 이진 파일 쓰기
```python
outfile = open("output.bin", "wb")
bytesArray = bytes([255, 128, 0, 1])
outfile.write(bytesArray)
outfile.close()
```

### 이미지 파일 복사 예제
```python
infile = open("123.png", "rb")
outfile = open("copy.png", "wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
```

---

## 🎯 임의 접근

```python
infile = open("test.txt", "r+")
str = infile.read(10)
print("읽은 문자열:", str)

position = infile.tell()      # 현재 위치 확인
print("현재 위치:", position)

infile.seek(0, 0)            # 파일 처음으로 이동
str = infile.read(10)
print("읽은 문자열:", str)

infile.close()
```

---

## 🗂️ 객체 입출력 (Pickle)

### 객체 저장
```python
import pickle

gameOption = {
    "Sound": 8,
    "VideoQuality": "HIGH",
    "Money": 100000,
    "WeaponList": ["gun", "missile", "knife"]
}

file = open("save.p", "wb")
pickle.dump(gameOption, file)
file.close()
```

### 객체 로드
```python
import pickle

file = open("save.p", "rb")
obj = pickle.load(file)
print(obj)
file.close()
```

---

## 📁 디렉토리 작업

```python
import os

# 현재 작업 디렉토리
dir = os.getcwd()

# 디렉토리 변경
os.chdir("data")

# 파일 목록
for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)

# 특정 확장자 파일 찾기
files = os.listdir()
for name in files:
    if os.path.isfile(name):
        if name.endswith(".jpg"):
            print(name)
```

---

## 🔍 정규식 (Regular Expression)

```python
import re

# 패턴 검색
text = "101 COM PythonProgramming"
numbers = re.findall("\d+", text)  # 모든 숫자 찾기
print(numbers)  # ['101']

# 줄 시작 패턴 찾기
f = open('uscons.txt')
for line in f:
    line = line.rstrip()
    if re.search('^[0-9]+', line):
        print(line)
f.close()

# 패턴 검사
if re.search("[a-z]", password):
    print("소문자 포함")
```

### 정규식 메타 문자
- `.` : 임의의 한 문자
- `*` : 0회 이상 반복
- `+` : 1회 이상 반복
- `\d` : 숫자
- `\w` : 문자
- `[0-9]` : 0부터 9까지의 숫자
- `^` : 줄의 시작
- `$` : 줄의 끝

---

## ⚠️ 예외 처리

### 기본 try-except 구조

```python
try:
    # 예외가 발생할 수 있는 코드
    z = x / y
except ZeroDivisionError:
    print("0으로 나누는 예외")
```

### 예외 메시지 출력

```python
try:
    z = x / y
except ZeroDivisionError as e:
    print(e)  # "division by zero"
```

### 주요 예외 종류
- `ZeroDivisionError` : 0으로 나누기
- `ValueError` : 부적절한 값
- `IOError` : 파일 입출력 오류
- `ImportError` : 모듈을 찾을 수 없음
- `KeyboardInterrupt` : 사용자 인터럽트
- `EOFError` : 파일의 끝

### 다중 예외 처리

```python
try:
    fh = open("testfile", "w")
    fh.write("테스트 데이터를 파일에 씁니다!!")
except IOError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
else:
    print("파일에 성공적으로 기록하였습니다.")
    fh.close()
```

### finally 블록

```python
try:
    f = open("test.txt", "w")
    f.write("테스트 데이터를 파일에 씁니다!!")
except IOError:
    print("Error: 파일을 찾을 수 없거나 데이터를 쓸 수 없습니다.")
finally:
    f.close()  # 예외 발생 여부와 관계없이 실행
```

### 예외 발생시키기

```python
raise NameError('Hello')
```

---

---

## 📝 핵심 요약

1. **파일 처리**: 파일을 열고(`open`), 작업하고, 닫는(`close`) 절차가 필요
2. **with 문**: 파일을 자동으로 닫아주는 안전한 방법
3. **텍스트/이진 파일**: 용도에 따라 적절한 모드 선택
4. **예외 처리**: `try-except` 블록으로 오류를 우아하게 처리
5. **정규식**: 패턴 매칭으로 복잡한 문자열 처리 가능

---
