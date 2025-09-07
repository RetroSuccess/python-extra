class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model= model
        self.year = year
        
    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
        
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
        
    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)   # inherit from Vehicle
        self.num_doors = num_doors
        
    def vehicle_info(self):   # overriding
        return f"{super().vehicle_info()} | Doors: {self.num_doors}"

        
class Bike(Vehicle):
    def __init__(self, make, model, year, engine_cc):
        super().__init__(make, model, year)   # inherit from Vehicle
        self.engine_cc = engine_cc

    def vehicle_info(self):   # overriding
        return f"{super().vehicle_info()} | Engine: {self.engine_cc}cc"
        
car = Car("Ford", "Mustang", 2021, 4)
bike = Bike("Honda", "CBR500R", 2020, 500)

print(car.vehicle_info())   # Output: 2020 Toyota Camry | Doors: 4
print(bike.vehicle_info())  # Output: 2019 Yamaha YZF-R3 | Engine: 321cc    