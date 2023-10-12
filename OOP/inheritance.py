#classes always start with an uppercase
class Person:
    def __init__(self,name, age, occupation,country,race):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.country = country
        self.race = race
    
    def greet(self):
        print("Hello", self.name)
    
    def cry(self):
        print(self.name, "cries alot!")
    
    def cry1(self):
        print(f"{self.name} is a cry baby! And he's {self.age} years old")


myPerson = Person("Jack", 76, "Lab Technician","Kenya","Black" )

print(myPerson.name)
print(myPerson.age)
print(myPerson.occupation)

myPerson.cry()
myPerson.cry1()

class Child(Person):
    def __init__(self,country,race,name,age,occupation):
        Person.__init__(self,country,race, name,age,occupation)

    def hello(self):
        print(f"My Name is {self.name}, I am From {self.country}")

mychild = Child("Kenya","Black","Jake",10,"Technician")

print(mychild.hello())

def hey(name):
    print("Hey",name)

hey(mychild.hello())


class School:
    def __init__(self,name,headTeacher,location):
        self.name = name
        self.headTeacher = headTeacher
        self.location = location


class Heads:
    def __init__(self,name,headTeacher,location):
        School.__init__(self,name,headTeacher,location)

    def displayHeads(self):
        Heads.displayHeads(self)

school1 = Heads("Kenya High School", "Mrs.Florah Mulatya", "Kileleshwa")
school2 = School("Riara Springs Girl's High School","Mrs.Jane Mulinge","Imara Daima")

print(school1.displayHeads())
