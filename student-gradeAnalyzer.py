student_grades = [("Alice", 89.5), ("Bob", 92.3), ("Charlie", 78.9), ("David", 85.6),('James', 87.2)]
allGrades= ([lis[1] for lis in student_grades])


def rtnHighest(allGrades):
    if (allGrades[0] > allGrades[1]):
        greatest1 = allGrades[0]
    else: greatest1 = allGrades[1]
    if (allGrades[2] > allGrades[3]):
        greatest2 = allGrades[2]
    else: greatest2 = allGrades [3]
    if(greatest1 > greatest2):
        greatest3 = greatest1
    else: greatest3 = greatest2
    if(allGrades[4] > greatest3):
        greatest = allGrades[4]
    else: greatest = greatest3
    highest = greatest
    return highest

def rtnLowest(allGrades):
    if (allGrades[0] < allGrades[1]):
            lowest1 = allGrades[0]
    else: lowest1 = allGrades[1]
    if (allGrades[2] < allGrades[3]):
        lowest2 = allGrades[2]
    else: lowest2 = allGrades [3]
    if(lowest1 < lowest2):
        lowest3 = lowest1
    else: lowest3 = lowest2
    if(allGrades[4] < lowest3):
        lowest = allGrades[4]
    else: lowest = lowest3
    return lowest

def grade_analyzer(student_grades, operation):
    student_grades = [("Alice", 89.5), ("Bob", 92.3), ("Charlie", 78.9), ("David", 85.6),('James', 87.2)]
    allGrades= ([lis[1] for lis in student_grades])
    average = (sum(allGrades)/4)
    if(operation == 'highest'):
        print(rtnHighest(allGrades))
    elif(operation == 'lowest'):
        print(rtnLowest(allGrades))
    elif(operation == 'average'):
        print(average)
    else:
        print('wrong function entered')
operation = input('Please enter operation(highest,lowest,average): ')

grade_analyzer(student_grades, operation)