# a dictionary is a collection which is unordered,

person = {
    "name": "John Doe",
    "age": 40,
    "nationality": "Kenyan",
    "occupation": "Student",
    "height": "1.69cm"
}

# print(person["name"])
# print(person.get("occupation"))

person["hobbies"]= "Hiking"

del person["name"]

person["age"]= 28 #reassignment in dictionaries.
print(person)

# print(person.keys())
# print(person.values())

xtra_features= {"Sex":"man", "race":"Latino"}

person.update(xtra_features)
# print(person)

for property in person:
    print(property)

for property in person:
    if person[property] == "Hiking":
        print("You Can Hike!")


def personValue(value):
    for property in person:
        if person[property] ==  value:
            print("The value is", value)
        else:
            print("The value doesn't exist!")

personValue("Kenya")
