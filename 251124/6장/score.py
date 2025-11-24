# 성적 입력받아 평균, 최대, 최소, 80점 이상 학생 수 출력하기
students = 5
list = []
count = 0

for i in range(students):
    value = int(input("성적 입력: "))
    list.append(value)

print("\n성적평균= ",sum(list)/len(list))
print("\n최고성적= ",max(list))
print("\n최저성적= ",min(list))

for score in list:
    if score >= 80:
        count += 1
print("\n80점 이상 학생 수= ",count)