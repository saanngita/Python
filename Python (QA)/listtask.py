# print("Welcome to the guest list management event.")
# print("You can perform upto 5 sction")
# print("1.add a guest")
# print("2.view all guest")
# print("3.remove a guest")
# print("exit")
# guest = []
# for x in range(5):
#     selectedguest = input("Enter a guest name:")
#     guest.append(selectedguest)
# print(guest)
# selectedguest = input("Do you want to  a remove guest? Yes or No")
# selectedguest.lower()
# if (selectedguest == "yes"):
#     removeguest = input("Enter the guestname to be removed.")
#     guest.remove(removeguest)
#     print(guest)
# else:
#     print(guest)

listitem = ["soap", "vegetable", "meat", "fish", "fan", "table", "grains", "ghee", "nuts", "milk", "cheese","tea","coffee"]
chooseitem = input("Which item do you want to buy? :")
if (chooseitem  in listitem):
    print("Item is available.")
else:
    print("Item is not available.")




