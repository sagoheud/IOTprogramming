'''
numbers = [1,2,3,4,5,6,7,8,9,10]
alist = numbers[::-2]
print(alist)

blist = remove.numbers[1:10]
print(blist)

del numbers[1:10]
print(numbers)

squares = []
for x in range(10):
    squares.append(x*x)
print(squares)
'''
list = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)


pita = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x*x + y*y == z*z]
print(pita)
'''
pita = []
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if x*x + y*y == z*z:
                pita.append((x,y,z))
print(pita)
'''