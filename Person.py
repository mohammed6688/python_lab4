class Person:
    mood = ("happy", "tired", "lazy")

    def __init__(self, name=None, money=0, mood=None, healthRate=0):
        self.name = name
        self.money = money
        self.mood = Person.mood.__getitem__(mood)
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if healthRate < 0:
            self.__healthRate = 0
        elif healthRate > 100:
            self.__healthRate = 100
        else:
            self.__healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= 10 * items
