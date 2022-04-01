class Car:
    def __init__(self, name=None, fuelRate=0, velocity=0):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate):
        if fuelRate < 0:
            self.__fuelRate = 0
        elif fuelRate > 100:
            self.__fuelRate = 100
        else:
            self.__fuelRate = fuelRate

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity < 0:
            self.__velocity = 0
        elif velocity > 200:
            self.__velocity = 200
        else:
            self.__velocity = velocity

    def run(self, distance, velocity):
        self.velocity = velocity
        self.fuelRate -= distance / 10  # fuel rate decrease by 10% every 10km distance
        self.stop(distance)

    def stop(self, distance):
        self.velocity = 0
        print(f"the remaining distance is {distance}")
