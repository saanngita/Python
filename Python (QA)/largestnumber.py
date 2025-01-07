mylist = []
for x in range(5):
  user_list = int(input("Enter the number you want to store in this list."))
  mylist.append(user_list)
print(mylist)
largest = max(mylist)
print(largest)
print("The largest number is:" +str(largest))
smallest = min(mylist)
print(smallest)
print("The smallest number is:" +str(smallest))

