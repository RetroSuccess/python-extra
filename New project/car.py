class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model                
        self.__make = make                
        self.__speed = 0             
        
    def accelerate(self):
        self.__speed += 5
        print(f"New speed: {self.__speed} mph")
        
    def brake(self):
        self.__speed -= 5
        print(f"New speed: {self.__speed} mph")
    
    def get_speed(self):
        return self.__speed
    

my_car = Car(2020, "Toyota")

print("Accelerating:")
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()

print("\nBraking:")
my_car.brake()
my_car.brake()  
my_car.brake()
my_car.brake()
my_car.brake()