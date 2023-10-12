import csv
filename = input("Enter Inventory File Name: ")
class Inventory:
    def __init__(self,name,Quantity, Price):
        self.name = name
        self.Quantity = Quantity
        self.Price = Price
        
    def add_item(self):
        count = 0
        while count <= 100:
            with open(filename, 'a') as file:
                file.write(f'{self.name},{self.Quantity},{self.Price}\n')
            count = count + 1
            break
    def remove_item(self):
        pass
    def update_item(self):
        with open(filename,"w+") as file:
            pass
            # append = file.writelines(int(input("Enter Line to Update: ")))
            # return append
    def display_inventory(self):
        with open(filename, "r") as file:
            print(file.read())
    
    # def loadtocsv(self):
    #     with open('inventory.csv', 'w', newline="") as inventory:
    #         writer = csv.writer(inventory)
    #         writer.writerow(['NAME','QUANTITY','PRICE'])
    #         for lines in filename:
    #             writer.writerow([lines.text])

goods = Inventory((input("Please enter Item Name: ")),(input("Please enter Quantity: ")),float(input("Please enter Price Ksh: ")))
goods.add_item()
goods.update_item()
goods.display_inventory()
# goods.loadtocsv()
# count = 0
# while count <= 2:
#     goods.add_item()
#     count = count + 1
#     break

