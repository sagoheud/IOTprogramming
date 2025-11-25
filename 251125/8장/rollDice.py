import random

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.value = 1

    def rollDice(self):
        self.__value = random.randint(1, 6)

    def getValue(self):
        return self.__value
    
    def __str__(self):
        return f"주사위 눈: {self.__value}"

d1 = Dice(10, 10)
d1.rollDice()
print(d1)