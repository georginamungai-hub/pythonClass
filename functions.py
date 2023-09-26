# def greet():
#     print('Hello Stranger!')

# greet()

# def greetings(name):
#     print('Hello', name)

# greetings('Chris')

#write a grade analyser function that takes the average score from a user and assigns a grade accordingly e.g 45 gets a C

# def gradeAssignment(averageScore):
   
#     print(averageScore)
#     if (averageScore >80 and averageScore <=100):
#         print('A')
#     elif(averageScore >70 and averageScore <=80):
#         print('B')
#     elif(averageScore >60 and averageScore <=70):
#         print('C')
#     elif(averageScore >50 and averageScore <=60):
#         print('D')
#     else:
#         print('E')  
# averageScore = float(input('Enter your average: '))
# gradeAssignment(averageScore)      


#square of a number

# def multiply (a, b):
#     return a * b

# print(multiply(134,3))

#write a function that calculates the area and perimeter of a rectangle

def areaPer(length, width):
    area = length * width
    perimeter = (length + width)*2
    return (area, perimeter)

length = float(input('Enter Length: '))
width = float(input('Enter Width: '))

print(areaPer(length, width))

    