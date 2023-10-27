class car:
    wheels = 4 # class variables
    def __init__(self,name,model,price,milage):
        # instance variables
        self.name = name
        self.model = model
        self.price = price
        self.milage = milage

    def compair(self, car2):
        if self.model == car2.model:
            return True
        else:
            return False

car.wheels = 5 # updated class or static variable that will change all objects same
car1 = car(name = "Kia", model = "Top end", price = 750000, milage = '30km/hr')
print("**********car1 details**********")
car1.name = "Tata" # updated instance variable of car1.name
print("car1 name = ", car1.name)
print("car1 model = ", car1.model)
print("car1 price = ",car1.price)
print("car1 milage = ",car1.milage)
print("car1 wheels = ",car.wheels)
car2 = car(name="Kia", model="Top end",price=950000,milage='50km/hr')
print("**********car2 details**********")
print("car2 name = ", car2.name)
print("car2 model = ", car2.model)
print("car2 price = ",car2.price)
print("car2 milage = ",car2.milage)
print("car2 wheels = ",car.wheels)
if car1.compair(car2):
    print("They are same model")
else:
    print("They are different model")