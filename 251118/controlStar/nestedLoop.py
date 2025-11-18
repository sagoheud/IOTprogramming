'''
rep = int(input("숫자 입력 : "))

for i in range(1,rep+1):
    for x in range(i):
        print("*", end="")
    print()
'''

'''
rep = int(input("숫자 입력 : "))

for i in range(1,rep+1):
    for x in range(rep-i):
        print(" ", end="")
    for x in range(i):
        print("*", end="")
    print()
'''

'''
n = int(input("정수를 입력하세요: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
'''

'''
n = int(input("정수를 입력하세요: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
'''


n = int(input("정수를 입력하세요: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()