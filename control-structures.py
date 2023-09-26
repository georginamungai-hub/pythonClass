#how to get input from a user
# name = input('Write your name, Please: ')
# print(name)

# height = int(input('Write your height, Please: '))
# age = int(input('Write Your Age: '))
# print(height + age)  

# age = int(input('Write Your Age please: '))

# if (age >= 18):
#     print("You're eligible to vote")
# else:
#     print('You cannot vote')

#write a simple program that determines whether the number input by a user is even or odd

# number = int(input('Please enter number: '))

# if(number % 2== 0):
#     print(number, 'is even')
# else:
#     print(number, 'is odd')

#write a grade analyser program that takes the average score from a user and assigns a grade accordingly

average = float(input('Please Enter Average Score: '))
print(average)

if (average >= 80.0):
    print('Your grade is A')
elif(average >=70.0):
    print('Your Grade is B')
elif(average >= 60.0):
    print('Your Grade is C')
elif(average >= 50.0):
    print('Your Grade is D')
else:
    print('Your Grade is E')