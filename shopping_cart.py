"""
Abbadi Anas
2025-01-27
This program simulates a simple shopping cart.  
Users can add items, specify quantities, and see the total cost. 
The program uses exception handling to manage invalid inputs.
"""
def Shopping():
    print("Welcome to the Shopping Cart Program !\n")
    while True:
        while True:
            try:
                num_Item = int(input("Hello! Can you provide how many items you want to get : "))
            except ValueError:
                print("Please enter a valid number")
                break
            total_price=[]
            total=0
            for i in range (num_Item):
                try : 
                    name=input(f"Can you insert the name of your item number {i+1}: ")
                    price = float(input(f"Can you insert the price of your item number {i+1}: "))
                    quantity = int(input(f"Can you insert the quantity of your item number {i+1}: "))
                    Cost = price * quantity
                    total_price.append(Cost)
                    print(f"The total price of your shop list of {quantity} {name}'s with each cost {price} is : {Cost}",)
                except ValueError:
                    print("You have submitted in a wrong way")
                    break
                break
            for i in range (len(total_price)):
                total = total+total_price[i] 
            print("The total price for everything you bought is :",total)
Shopping()