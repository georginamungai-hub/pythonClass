# #while loops
# #boolean = true, false

# while True:
#     print('Hello World')
#     break

# number = 2
# while(number < 20):
#     print('Number is less than 20')
#     break

# #for loop
# for i in range (2,50):
#     print(i)

#write a for loop that prints number  between 6 and 100
# print('yes')
# for i in range (0,100):
#     if (i%2==0):
#         print(i, 'is even')
    
#write a python program that prints odd numbers between 0 and 20

# for num in range(0,20):
#     if (num%2 != 0):
#         print(num, 'is odd')

#write a python program that prints all multiples of 7 between 0 and 1000
for num2 in range (0,1000,7):
    print(num2)


def evenNumbers(n):
    for i in range (n):
        if(i%2 ==0):
            print(i, 'is even')
evenNumbers(200)