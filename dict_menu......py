print("Welcome to the Resturant!")
print("Menu:")
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 200,
    "Salad": 150,
    "Fries": 80,
    }
for x in menu:
    print(f"{x}: Rs.{menu[x]}")
bill_amt = 0
orderlist = []
print("Enter the name of the dish you'd like to order. Type 'done' to finish.")
for x in range(5):
    order_dish = input("Dish:")
    if order_dish == "done":
        break
    elif order_dish in menu:
        orderlist.append(order_dish)
        bill_amt = (menu[order_dish]) + bill_amt
        print(f"{order_dish} added to your order. Price: Rs{menu[order_dish]}")
    else:
        print("Sorry we don't serve")
print("Your Order Summary:")
print("Dish             Price")
print("----------------------")
for x in orderlist:
    print(f"{x}           {menu[x]}")
print("----------------------")    
total_amt = bill_amt
print(f"Total Amount : {total_amt} ")
 
       
    
                      