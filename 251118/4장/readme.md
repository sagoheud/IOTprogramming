# 파이썬 익스프레스 - 4장 요약

## 📚 반복문 (Loop Statements)

### 학습 목표

- ✅ 반복문의 필요성을 이해한다
- ✅ for 문을 사용하여 정해진 횟수만큼 반복하는 방법을 학습한다
- ✅ range() 함수를 이해하고 사용할 수 있다
- ✅ while 문을 사용하여 조건으로 반복하는 방법을 학습한다
- ✅ 중첩 반복문의 개념을 이해한다
- ✅ 무한 루프가 사용되는 환경을 이해한다

---

## 🔁 반복문의 필요성

### 반복을 사용하지 않을 때

```python
print("방문을 환영합니다!")
print("방문을 환영합니다!")
print("방문을 환영합니다!")
print("방문을 환영합니다!")
print("방문을 환영합니다!")
```

### 반복을 사용할 때

```python
for i in range(5):
    print("방문을 환영합니다!")
```

💡 **1000번 출력해야 한다면?** 반복문 없이는 불가능!

---

## 🎯 반복의 종류

### 1. 횟수 반복 (for 문)

정해진 횟수만큼 반복

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### 2. 조건 반복 (while 문)

특정 조건이 만족되는 동안 반복

```python
count = 0
while count < 5:
    print(count)
    count += 1  # 0, 1, 2, 3, 4
```

---

## 📋 리스트 기초

### 리스트란?

항목들을 저장하는 자료 구조

```python
# 리스트 생성
slist = ["영어", "수학", "사회", "과학"]

# 리스트 항목 접근 (인덱스는 0부터 시작)
print(slist[0])   # "영어"
print(slist[1])   # "수학"
print(slist[-1])  # "과학" (마지막 항목)

# 리스트 항목 변경
slist[0] = "국어"
print(slist)  # ["국어", "수학", "사회", "과학"]
```

### 동적으로 항목 추가

```python
mylist = []  # 빈 리스트 생성
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)  # [1, 2, 3]
```

---

## 🔄 for 문 (횟수 반복)

### 기본 구조

```python
for 변수 in 시퀀스:
    반복할_문장
```

### 리스트를 이용한 반복

```python
# 리스트의 각 항목에 대해 반복
for item in ["영어", "수학", "사회"]:
    print(item)

# 출력:
# 영어
# 수학
# 사회
```

### 숫자 리스트로 반복

```python
for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")  # 1 2 3 4 5
```

---

## 📐 range() 함수

### range() 함수란?

연속된 정수를 자동으로 생성하는 함수

### 사용 방법

```python
# 1. range(끝): 0부터 끝-1까지
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# 2. range(시작, 끝): 시작부터 끝-1까지
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5

# 3. range(시작, 끝, 간격): 시작부터 끝-1까지 간격만큼 증가
for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9

# 4. 역순으로 반복
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
```

### range() 함수 비교

| 형식 | 예시 | 결과 |
|------|------|------|
| `range(n)` | `range(5)` | 0, 1, 2, 3, 4 |
| `range(start, end)` | `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(start, end, step)` | `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(start, end, -step)` | `range(10, 0, -1)` | 10, 9, 8, ..., 1 |

---

---

## ⏱️ while 문 (조건 반복)

### 기본 구조

```python
while 조건식:
    반복할_문장
```

### else가 있는 while 문

```python
i = 0
while i < 3:
    print("루프 안쪽")
    i = i + 1
else:
    print("else 부분")

# 출력:
# 루프 안쪽
# 루프 안쪽
# 루프 안쪽
# else 부분
```

---

## ⚠️ 무한 루프

### 무한 루프 오류

```python
# 잘못된 예 - 무한 루프
i = 0
while i < 10:
    print("Hello!")  # i가 증가하지 않아 무한 반복!
```

### 의도적인 무한 루프

```python
# 올바른 무한 루프 사용
while True:
    command = input("명령 입력 (종료: q): ")
    if command == 'q':
        break
    print(f"입력: {command}")
```

---

## 🔁 중첩 반복문 (Nested Loop)

### 개념

반복문 안에 또 다른 반복문이 있는 구조

```python
for 외부변수 in 범위1:
    for 내부변수 in 범위2:
        반복할_문장
```

---

## 🛑 break와 continue

### break: 반복문 즉시 종료

```python
while True:
    light = input('신호등 색상을 입력하시오: ')
    if light == 'green':
        break
print('전진!!')

# 입력: red
# 입력: yellow
# 입력: green
# 출력: 전진!!
```

### continue: 다음 반복으로 건너뛰기

```python
for i in range(1, 11):
    if i % 3 == 0:  # 3의 배수이면
        continue    # 건너뛰기
    print(i, end=" ")

# 출력: 1 2 4 5 7 8 10
```

### break vs continue 비교

| 키워드 | 동작 | 사용 시기 |
|--------|------|-----------|
| `break` | 반복문 완전히 종료 | 목표를 달성했거나 오류 발생 시 |
| `continue` | 현재 반복만 건너뛰고 다음 반복 진행 | 특정 조건의 경우만 제외하고 싶을 때 |

---

---

## 📊 for vs while 비교

| 특성 | for 문 | while 문 |
|------|--------|----------|
| **사용 시기** | 반복 횟수가 정해진 경우 | 조건이 만족될 때까지 반복 |
| **구조** | `for 변수 in 범위:` | `while 조건:` |
| **장점** | 간결하고 명확 | 유연한 조건 설정 |
| **예시** | 1~100까지 출력 | 목표 금액 달성까지 반복 |

### 같은 동작을 다른 방법으로

```python
# for 문 사용
for i in range(5):
    print(i)

# while 문 사용
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 🎯 반복문 선택 가이드

### for 문을 사용하는 경우
- ✅ 정확한 반복 횟수를 알 때
- ✅ 리스트나 시퀀스를 순회할 때
- ✅ 범위가 명확할 때

```python
# 예시
for i in range(10):           # 10번 반복
for item in my_list:          # 리스트 순회
for i in range(1, 100, 2):    # 홀수만
```

### while 문을 사용하는 경우
- ✅ 반복 횟수를 모를 때
- ✅ 특정 조건이 만족될 때까지 반복
- ✅ 사용자 입력에 따라 종료해야 할 때

```python
# 예시
while money < goal:           # 목표 달성까지
while password != correct:    # 올바른 입력까지
while True:                   # 무한 루프 (break 필요)
```

---

## 💡 반복문 작성 팁

### ✅ DO (권장)

1. **명확한 종료 조건 설정**
```python
# 좋은 예
count = 0
while count < 10:
    print(count)
    count += 1  # 종료 조건을 위한 증가
```

2. **의미 있는 변수명 사용**
```python
# 좋은 예
for student in students:
    print(student.name)
```

3. **적절한 들여쓰기**
```python
# 좋은 예
for i in range(5):
    print(i)
    if i % 2 == 0:
        print("짝수")
```

### ❌ DON'T (비권장)

1. **무한 루프 주의**
```python
# 나쁜 예
i = 0
while i < 10:
    print(i)
    # i를 증가시키지 않음!
```

2. **너무 깊은 중첩 피하기**
```python
# 나쁜 예 (4중 중첩)
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):  # 너무 깊음!
                # ...
```

3. **반복문 내 불필요한 계산**
```python
# 나쁜 예
for i in range(1000):
    result = expensive_calculation()  # 매번 같은 계산

# 좋은 예
result = expensive_calculation()  # 한 번만 계산
for i in range(1000):
    use(result)
```

---

## 📋 핵심 요약

### 기본 구조

```python
# for 문
for 변수 in 범위:
    반복할_코드

# while 문
while 조건:
    반복할_코드

# 중첩 반복문
for i in range(외부범위):
    for j in range(내부범위):
        반복할_코드

# break와 continue
for i in range(10):
    if 조건1:
        break      # 반복문 종료
    if 조건2:
        continue   # 다음 반복으로
    실행코드
```

### range() 함수 정리

| 형식 | 의미 | 예시 |
|------|------|------|
| `range(n)` | 0부터 n-1까지 | `range(5)` → 0,1,2,3,4 |
| `range(a, b)` | a부터 b-1까지 | `range(2, 7)` → 2,3,4,5,6 |
| `range(a, b, c)` | a부터 b-1까지 c씩 증가 | `range(0, 10, 2)` → 0,2,4,6,8 |

---

## 🎯 연습 문제

1. **역순 출력**: 10부터 1까지 역순으로 출력
2. **짝수 합계**: 1부터 100까지 짝수의 합 계산
3. **배수 찾기**: 1부터 50까지 3의 배수 출력
4. **별 피라미드**: 높이를 입력받아 별 피라미드 출력
5. **최댓값 찾기**: 사용자가 입력한 숫자 중 최댓값 찾기 (0 입력 시 종료)
6. **완전수 찾기**: 1부터 1000까지 완전수 찾기
7. **피보나치 수열**: n번째 피보나치 수 출력
8. **로또 번호 생성**: 1~45 중 중복 없이 6개 출력
9. **성적 평균**: 학생 수를 입력받고 평균 계산
10. **역삼각형 패턴**: 별로 역삼각형 그리기

---

## ✅ 학습 점검

- [ ] for 문의 기본 구조 이해
- [ ] range() 함수의 3가지 형식 숙지
- [ ] while 문의 기본 구조 이해
- [ ] 무한 루프와 종료 조건의 중요성 인식
- [ ] break와 continue의 차이점 이해
- [ ] 중첩 반복문 작성 및 이해
- [ ] for와 while의 적절한 사용 시기 판단
- [ ] 리스트와 반복문의 결합 이해
- [ ] 실전 문제 해결 능력 향상

---

## 🔑 핵심 개념 카드

### 반복문 4대 원칙

1. **초기화**: 반복 전 변수 초기화
2. **조건**: 명확한 반복 조건 설정
3. **실행**: 반복할 코드 작성
4. **증감**: 종료 조건을 위한 변수 변경

```python
# 완벽한 while 문 예시
i = 0              # 1. 초기화
while i < 10:      # 2. 조건
    print(i)       # 3. 실행
    i += 1         # 4. 증감
```

---
