# file = open('words.txt', 'r')

# for line in file:
#     print(line)

#     or


# with open('words.txt', 'r') as file:
#     for line in file:
#         print(line)

lines = ['Welcome','Cow', 'Cat', 'Jake']
with open('text.txt', 'w') as textfile:
    textfile.writelines(lines)        