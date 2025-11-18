# 수를 입력받고, 해당 수의 구구단을 출력하는 프로그램
'''
print(f"구구단 계산")
x = int(input("정수 x 입력: "))
y = int(input("정수 y 입력: "))

if x in range(1,10):
    if y in range(1, 10):
        sum = x * y
        print(f"x곱하기 y는 {sum}입니다.")
    else:
        print(f"y에 1에서 9사이의 정수를 입력하세요.")
else:
    print(f"x에 1에서 9사이의 정수를 입력하세요.")
'''

print(f"구구단 계산")
dan = int(input("단 입력: "))
if 1 <= dan <= 9:
    for i in range(1,10):
        print(f"{dan} X {i} = {dan*i}")
else:
    print(f"1부터 9사이 수를 입력하세요.")