# 정수를 입력받아 등급을 출력하는 프로그램을 작성하시오.
# 90점이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 은 F

score = int(input("점수 입력: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수는 {score}이고 등급은 {grade} 입니다.")


'''
score = int(input("점수 입력: "))

match score // 10:
    case 10 | 9:
        grade = "A"
    case 8:
        grade = "B"
    case 7:
        grade = "C"
    case 6:
        grade = "D"
    case _:
        grade = "F"

print(f"점수는 {score}이고 등급은 {grade} 입니다.")
'''