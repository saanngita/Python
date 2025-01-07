smallpizza=300
mediumpizza=400
largepizza=500
bill_amt=0
pizza_choice=input("enter the size of pizza:")
print(" enter s for smallpizza, m for medium pizza,l for large pizza")

if pizza_choice=="s":
    print("you have chose small pizza")
    bill_amt=smallpizza
    print("bill amt. is:",bill_amt)

elif pizza_choice=="m":
    print("you have chose medium pizza:")
    bill_amt=mediumpizza
    print("bill amt. is:",bill_amt)

elif pizza_choice=="l":
    print("you have chose large pizza:")
    bill_amt=largepizza
    print("bill amt. is:",bill_amt)
else:
    print("your choice is invalid")

