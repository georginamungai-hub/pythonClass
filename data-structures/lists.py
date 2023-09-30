#lists also store information - []

names = ['Jake', 'Jack', 'Jax']
number =[1] # for a tuple you don't have to have a comma at the end when representing 1 number


mixed = ['Car', 1 ,2.5, True, 'Kenya'] #can be used to represent more than one data type

#to access information in an array/list, you use indexing- index is a position in an array

print(mixed[0])

#you can append an array:

mixed[3] = False

print(mixed)

for item in mixed:
    print(item)


listTuple = [(1,2), ('name', 12), ('day', 23)]