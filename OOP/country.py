class Country:
    def __init__(self, name, population, location):
        self.name = name
        self.population = population
        self.location = location
    
    def pinLocation(self):
        if (self.location == "Asia"):
            print(f"{self.name} is north of Kenya")
        elif (self.location == "SouthAmerica"):
            print(f"{self.name} is West of Kenya")
        elif(self.location == "Australia"):
            print(f"{self.name} is East of Kenya")
        else:
            print(f"{self.name} cannot be located!")

    def describePopulation(self):
        if(int(self.population)> 40000000):
            print(f"{self.name} is overpopulated")
        else:
            print(f"{self.name} is underpopulated")

myCountry = Country(
    input("Please Enter Country Name: "),
    input("Please Enter Country's Population: "),
    input("Please Enter Country's Continent: ")
)

myCountry.pinLocation()
myCountry.describePopulation()