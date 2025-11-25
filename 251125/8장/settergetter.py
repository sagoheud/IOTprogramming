class Television:
    serialNumber = 0

    def __init__(self,channel,volume,power):
        self.__channel = channel
        self.__volume = volume
        self.__power = power

    def setChannel(self, channel):
        self.__channel = channel
        Television.Number(self)
    def getChannel(self):
        return self.__channel
    
    def setVolume(self, volume):
        self.__volume = volume
        Television.Number(self)
    def getVolume(self):
        return self.__volume
    
    def setPower(self, power):
        self.__power = power
        Television.Number(self)
    def getPower(self):
        return self.__power
    
    def Number(self):
        Television.serialNumber += 1
        self.__number = Television.serialNumber
        return self.__number
        
    
    def show(self):
        power_state = "On" if self.__power else "Off"
        print(f"Channel: {self.__channel}, \
            Volume: {self.__volume}, \
            Power: {power_state}, \
            Number: {Television.Number(self)}")

print(Television.serialNumber)  # Output: 0
tv = Television(5, 10, True)
tv.show()
tv.setChannel(15)
tv.setVolume(25)
tv.setPower(False)
tv.show()
tv = Television(10, 20, True)
tv.show()