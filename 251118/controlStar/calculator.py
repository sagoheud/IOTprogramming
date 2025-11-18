import random

z = random.randint(1,2)
x = random.randint(1,100)
y = random.randint(1,100)

if z == 1:
    answer = int(input(f"{x} + {y} = "))
    if answer == x + y:
        print("정답")
    else:
        print("오답")
else:
    answer = int(input(f"{x} - {y} = "))
    if answer == x - y:
        print("정답")
    else:
        print("오답")