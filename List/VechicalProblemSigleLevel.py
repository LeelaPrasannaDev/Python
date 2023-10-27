class Vehicle:
    def __init__(self, make, model, year, milage):
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage

    def get_info(self):
        return self.make, self.model, self.year, self.milage


class Car(Vehicle):
    def __init__(self, fuel_type, make, model, year, milage):
        super().__init__(make, model, year, milage)
        self.fuel_type = fuel_type

    def display_car_info(self):
        return self.fuel_type, self.make, self.model, self.year, self.milage


c1 = Car('petrol', 'Tata', 'Top end', '2023', '20 km/h')
inf = c1.get_info()
print("Company Of Vechile= ", inf[0])
print("Model = ", inf[1])
print("Year = ", inf[2])
print("Milage = ", inf[3])
cinfo = c1.display_car_info()
print("Company Of Vechile= ", cinfo[1])
print("Model = ", cinfo[2])
print("Year = ", cinfo[3])
print("Milage = ", cinfo[4] )
print("Fuel type  = ", cinfo[0])