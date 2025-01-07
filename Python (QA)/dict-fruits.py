fruits = {
    "banana" : 100,
    "apple" : 150,
    "kiwi" : 200,
    }
#check if "orange" exists in theb dictionary.
if "orange" in fruits:
    print("Orange exists in dictionary.")
else:
    print("Orange is not exist in dictionary.")
#add orange with a price 50.
    fruits["orange"] = 50
print(fruits)
if "apple" in fruits:
    print("Apple is exists in dictionary.")
#update the price of "apple" to 120.
    fruits.update({"apple": 120})
else:
    print("Apple is not exists in dictionary.")
print(fruits)
if "banana" in fruits:
    print("Banana is exist in dictionary.")
#delete "banana" from fruits.
    del fruits["banana"]
else:
    print("Banana is not exist in dictionary.")
print(fruits)    
