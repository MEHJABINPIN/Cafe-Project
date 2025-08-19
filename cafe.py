menu = {
            'Coffee':40,
            'Pasta':60,
            'Tea':20,
            'Maggie':50,
            'Fries':80,
            'Burger': 80,
            'Pizza':199
        }
print("Welcome to our Cafe !!")
print(" Coffee : Rs 40 \n Pasta : Rs 60 \n Tea : Rs 20 \n Maggie : Rs 50 \n Fries : Rs 80 \n Burger : Rs 80 \n Pizza : Rs 199")

# order Total
Total = 0
# order 
order = input("Enter your Order : ")
if order in menu :
    print("Your order is Preparing... ")
    Total +=menu[order]
if order not in menu:
    print(f"Sorry but this {order} currently not available. ")
  

# another order 
Total1 = 0    
another_order = input("Do you want to order something else ? (Yes/No) :")
item = input("Enter Your Order : ")
if item in menu :
    print("Your item is added... ")
    Total1 +=menu[item]
else:
    print("Sorry this item currently not available. ")   
Bill = Total + Total1
print("Your Total  Amount is : Rs",Bill)         