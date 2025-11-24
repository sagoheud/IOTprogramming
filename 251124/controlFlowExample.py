# control_flow_example.py

# 1. 조건문 (Conditional Statements): if, elif, else
## 주어진 점수에 따라 등급을 출력하는 예시

print("--- 1. 조건문 (if, elif, else) ---")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수: {score}, 등급: {grade}\n")


# 2. 반복문 (Loop Statements): while
## 1부터 5까지 숫자를 출력하는 예시

print("--- 2. 반복문 (while) ---")
count = 1
while count <= 5:
    print(f"현재 숫자 (while): {count}")
    count += 1
print("\n")


# 3. 반복문 (Loop Statements): for
## 리스트의 항목을 하나씩 출력하는 예시

print("--- 3. 반복문 (for) ---")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"현재 과일 (for): {fruit}")
print("\n")

# for와 range() 함수를 이용해 1부터 5까지 숫자를 출력하는 예시 (5는 포함되지 않음)
print("--- 3. 반복문 (for) + range() ---")
for i in range(1, 6): # range(시작, 끝+1)
    print(f"현재 숫자 (for/range): {i}")
print("\n")


# 4. 루프 제어문 (Loop Control Statements): break
## 10까지 세는 중 5에서 멈추는 예시

print("--- 4. 루프 제어문 (break) ---")
for num in range(1, 11):
    if num == 6:
        print("num이 6이므로 반복을 멈춥니다 (break).")
        break
    print(f"현재 숫자 (break 예제): {num}")
print("\n")


# 5. 루프 제어문 (Loop Control Statements): continue
## 짝수만 출력하고 홀수는 건너뛰는 예시

print("--- 5. 루프 제어문 (continue) ---")
for num in range(1, 11):
    if num % 2 != 0: # num이 홀수라면
        print(f"홀수 {num}은 건너뜁니다 (continue).")
        continue
    print(f"현재 짝수 (continue 예제): {num}")
print("\n")


# 6. 복합적인 예시: 리스트 컴프리헨션 (List Comprehension)
## for와 if를 한 줄로 사용하여 1부터 10까지의 숫자 중 짝수만 포함하는 리스트를 생성

print("--- 6. 복합적인 예시: 리스트 컴프리헨션 ---")
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"1부터 10까지의 짝수 리스트: {even_numbers}")