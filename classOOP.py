class Classroom():
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_code(self):
        return self.code
    
    def set_name(self, code):
        if code > 1:
            return self.code
        else:
            print("Failer")
        
    def get_credits(self):
        return self.credits
        
    def set_credits(self, credits):
        if credits > 1:
            self.credits = credits
        else:
            print("Error")
            
classroom = Classroom("Amy", 5, 1.0)

print("Name: ", classroom.get_name())
print("Code: ", classroom.get_code())
print("Credits: ", classroom.get_credits())    

class Student(Classroom):
    def fight(self):
        print("I am fighting")
        
s = Student("Bob", 10, 2.0)
s.get_name()
print(s.get_name())
s.fight()

class Animal:
   def speak(self):
      return "Animal speaks!"
class Dog(Animal):
    def speak(self):  # Overriding the speak method
          return "Dog barks!"
dog = Dog()
print(dog.speak())  # Output: Dog barks!

