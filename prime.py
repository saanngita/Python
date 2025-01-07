num = int(input("Enter a number.:"))
num_count = 0
for x in range(1,num+1):
    if num % x == 0:
       num_count = num_count + 1
if num_count == 2:
   print(num,"It is prime number")
else:
   print(num,"It is not prime number")
print("Hello i am kavya")   