'''
 Write a Python program to create a person class.
  Include attributes like name, country and date of birth.
  Implement a method to determine the person's age.
'''
from datetime import date


class Person:
    def __init__(self, name, country, dateOfBirth):
        self.name = name
        self.country = country
        self.dateOfBirth = dateOfBirth

    def toFindPersonAge(self):
        today = date.today()
        age = today.year - self.dateOfBirth.year
        if today < date(today.year, self.dateOfBirth.month, self.dateOfBirth.day):
            age -= 1
        return age


person1 = Person('Venky', 'India', date(1999, 5, 15))
person2 = Person('Vyshu', 'India', date(2002, 7, 8))

print('Name of person1 = ', person1.name)
print('Country of person1 = ', person1.country)
print('Date of birth of person1 = ', person1.dateOfBirth)
print('Age of person1 = ', person1.toFindPersonAge())
print('Name of person2 = ', person2.name)
print('Country of person2 = ', person2.country)
print('Date if birth of person2 = ', person2.dateOfBirth)
print('Age of person2 = ', person2.toFindPersonAge())
