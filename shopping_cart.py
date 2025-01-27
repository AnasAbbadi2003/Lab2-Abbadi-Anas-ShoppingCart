"""
Abbadi Anas
2025-01-27
This program simulates a simple shopping cart.  
Users can add items, specify quantities, and see the total cost. 
The program uses exception handling to manage invalid inputs.
"""
print("Welcome to the Shopping Cart Program !\n")

num_Item = int(input("Hello! Can you provide how many items you want to get : "))

for i in range (num_Item):
    try :
        
        name=input(f"Can you insert the name of your item number {i+1}:")
        if type(name)!='str':
            raise ValueError()
        price = float(input(f"Can you insert the price of your item number {i+1}:"))
        quantity = int(input(f"Can you insert the quantity of your item number {i+1}:"))
    except  ValueError:
        print("You have submitted in a wrong way")
        break