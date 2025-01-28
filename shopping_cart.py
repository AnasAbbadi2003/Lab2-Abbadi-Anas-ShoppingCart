"""
Abbadi Anas
2025-01-27
This program simulates a simple shopping cart.  
Users can add items, specify quantities, and see the total cost. 
The program uses exception handling to manage invalid inputs.
"""
# a function wich returns the total of the shopping items
def Shopping():
    print("Welcome to the Shopping Cart Program !\n")
    # loop to repeat the code if an error occurs
    while True:
        while True:
            # asking the user to enter how many item he wants
            try:
                num_Item = int(input("Hello! Can you provide how many items you want to get : "))
                if num_Item <=0:
                    raise ValueError()
            except ValueError:
                print("Please enter a valid number")
                break
            # a list that will have the total of each list
            total_price=[]
            total=0
            # a loop that asks the user to enter informations depending on how many items he wants
            for i in range (num_Item):
                try : 
                    # asking for the name of the product
                    name=input(f"Can you insert the name of your item number {i+1}: ")
                    # asking for the Price of the product
                    price = float(input(f"Can you insert the price of your item number {i+1}: "))
                    # asking for the quantity of the product
                    quantity = int(input(f"Can you insert the quantity of your item number {i+1}: "))
                    # counting the cost of one of the lists
                    Cost = price * quantity
                    # inserting the cost in the total_price=[] list
                    total_price.append(Cost)
                    # printing the cost and the item informations for one list
                    print(f"The total price of your shop list {i+1} of {quantity} {name}'s with each cost {price} is : {Cost}",)

                    prob = False
                    prob2= False
                    # let the user chose either to proceed with the item or not
                    agree = input(f'Do you want to proceed with the list number :{i+1} : (Y/N) ? ').lower()
                    if agree != 'y':
                        prob2 = True
                        break
                except ValueError:
                    prob = True
                    break
            if prob2 == True:
                print("You can retry again !")
                break
            if prob == True:
                print("You have submitted in a wrong way")    
                break
            # counting the sum of all of the items cost
            for i in range (len(total_price)):
                total += total_price[i] 
                return total
#give the total_price variable the value "total" 
total_price=Shopping()
# printing the total cost
print("The total price for everything you bought is :",total_price)
# ask the repeat weither he wants to reuse the shopping system or not
repeat = input("Would You like to repeat (Y/N)? ").lower()
if repeat != 'y':
    print("Well thank you for using our shopping system .")
else:
    Shopping()