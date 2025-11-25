class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rect(self.width + other.width, self.height + other.height)
    def __eq__(self, value):
        return self.width * self.height == value.width * value.height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
r1 = Rect(4, 5)
r2 = Rect(5, 4)
r3 = r1 + r2
print(f"r1의 넓이 = {r1.area()}, r1의 둘레 = {r1.perimeter()}")
print(f"r2의 넓이 = {r2.area()}, r2의 둘레 = {r2.perimeter()}")
print(f"r3의 넓이 = {r3.area()}, r3의 둘레 = {r3.perimeter()}")
'''
if r1 == r2:
    print("r1과 r2는 면적이 같습니다.")
else:
    print("r1과 r2는 면적이 다릅니다.")
'''

print("r1과 r2는 면적이 같습니다.") if r1 == r2 else print("r1과 r2는 면적이 다릅니다.")