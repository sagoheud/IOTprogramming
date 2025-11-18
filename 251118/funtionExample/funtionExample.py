import math

def circleArea(radius): # parameter 매개변수 2 usages
    area = math.pi * radius * radius
    return area

circle1 = circleArea(5) # parameter 인자
circle2 = circleArea(10)

print(circle1)
print(circle2)
