'''
while True:
    z = input("초록색은 무엇입니까?")
    if z =='green':
        break
print("정답")
'''

for i in range(1,101):
    if i < 2:
        continue

    is_prime = True
    for l in range(2, i):
        if i % l == 0:
            is_prime = False
            break

    if not is_prime:
        continue

    print(i, end=" ")