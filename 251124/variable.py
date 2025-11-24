# 간단한 변수 예제 - /c:/00python/basic/251124/variable.py

# 숫자형
age = 30
pi = 3.14159

# 문자열
name = "홍길동"
greeting = f"안녕하세요, {name}님. 나이는 {age}세입니다."

# 불리언과 None
is_student = False
nothing = None

# 여러 변수 동시 할당
x, y, z = 1, 2, 3

# 값 교환 (스왑)
a = 10
b = 20
a, b = b, a  # a=20, b=10

# 컬렉션 변수 예제
fruits = ["사과", "바나나", "체리"]
person = {"이름": name, "나이": age, "학생인가요": is_student}

# 상수(관례)
PI = 3.14159

# 출력으로 확인
print(greeting)
print("pi:", pi, "PI:", PI)
print("x, y, z:", x, y, z)
print("a, b (swap):", a, b)
print("fruits:", fruits)
print("person:", person)
print("nothing:", nothing)

# 타입 확인과 간단한 연산
print("type of age:", type(age))
age += 1  # 나이 1 증가
print("한 해 뒤 나이:", age)