class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    def getMake(self):
        return self.make
    def setMake(self, make):
        self.make = make
    def getDesc(self):
        return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}"

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize
    def getBatterySize(self):
        return self.batterySize
    def setBatterySize(self, batterySize):
        self.batterySize = batterySize
    # def getDesc(self):
    #     return f"차량 = {self.make}, {self.model}, {self.color}, {self.price}, {self.batterySize}"
        
c1 = Car("V1","Victory","흰색","10")
c2 = ElectricCar("V2","Tesra","검은색","30","20")

print(c1.getDesc())
print(c2.getDesc())