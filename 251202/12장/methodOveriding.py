import math

class Shape:
    def __init__(self):
        pass
    def draw(self):
        print("Shape 클래스의 draw() 메소드가 호출되었습니다.")    
    def getArea(self):
        print("Shape 클래스의 getArea() 메소드가 호출되었습니다.")
        
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius       
    def draw(self):
        super().draw()
        print("Circle 클래스의 draw() 메소드가 호출되었습니다.")      
    def getArea(self):
        return math.pi * self.radius ** 2
    
c1 = Circle(10)
c1.draw()
print(f"원의 면적은 {c1.getArea()} 입니다.")