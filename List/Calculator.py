"""
 Write a Python program to create a calculator class.
  Include methods for basic arithmetic operations.
"""


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 - self.num2

    def division(self):
        return self.num1 / self.num2

    def modular_division(self):
        return self.num1 % self.num2

    def average(self):
        return (self.num1 + self.num2) / 2


cal = Calculator(60, 90)
print('Addition of two given numbers = ', cal.addition())
print('Subtraction of two given numbers = ', cal.subtraction())
print('Multiplication of two given numbers = ', cal.multiplication())
print('Division of two given numbers = ', cal.division())
print('Modular division of two given numbers = ', cal.modular_division())
print('Average of two given numbers = ', cal.average())
