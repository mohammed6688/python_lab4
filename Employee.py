from Car import Car
from Person import Person
import re


class Employee(Person):
    def __init__(self, email, distanceToWork, salary=1000, name=None, money=0, mood=None, healthRate=None):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = Car()
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            self.__salary = 1000
        else:
            self.__salary = salary

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            self.__email = email
        else:
            print("you entered wrong email format\n")

    def work(self, hours):
        if hours == 8:
            self.mood = super().mood.__getitem__('happy')
        elif hours > 8:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def drive(self, distance, velocity):
        self.car.run(distance, velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        pass
