#  "Smart Budget Tracker"
# Objective: Create a Python program that tracks a user's expenses and generates reports on their spending habits.
# Requirements:
# User should be able to input different expenses with categories (e.g. food, transportation, entertainment, etc.)
# User should be able to view their expenses and the total amount spent in each category
# User should be able to view their overall spending and the total amount saved
# The program should provide a monthly spending report and an annual report
# The program should be able to suggest a budget for each category based on the user's expenses


class Expenses:
    def __init__(self,commodity,cost):
        self.commodity = commodity
        self.cost = cost

class ExpenseTracker:
    def __init__(self,commodity,cost):
        Expenses.__init__(self,commodity,cost)
        self.Expenses = []
    
    def addExpense(self):
        count = 0
        while count < 2:
            expense = ExpenseTracker((input("Enter Commodity Name: ")),int(input("Enter Cost: ")))
            count = count + 1
        self.Expenses.append(expense)
        

    def viewExpense(self):
        for item in self.Expenses:
            print(item)
        

mytracker = ExpenseTracker((input("Enter Commodity Name: ")),int(input("Enter Cost: ")))
mytracker.addExpense()
mytracker.viewExpense()

    