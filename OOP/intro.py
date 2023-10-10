#classes always start with an uppercase
class Person:
    def __init__(self,name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def greet(self):
        print("Hello", self.name)
    
    def cry(self):
        print(self.name, "cries alot!")
    
    def cry1(self):
        print(f"{self.name} is a cry baby! And he's {self.age} years old")


myPerson = Person("Jack", 76, "Lab Technician")

print(myPerson.name)
print(myPerson.age)
print(myPerson.occupation)

myPerson.cry()
myPerson.cry1()