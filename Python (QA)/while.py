# i=1
# while i<=20:
#     if i%2 != 0:
#       print(i)
#     i += 1 



num = int(input("Enter any number."))
for x in range(0,num):
    if x%3==0 and x%5==0:
       print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)