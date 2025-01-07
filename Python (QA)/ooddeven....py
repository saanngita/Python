# oddNumber_count = 0
# evenNumber_count = 0
# for x in range(5):
#     number = int(input("Enter number"))
#     if number%2==0:
#         evenNumber_count = evenNumber_count + 1
#     else:
#         oddNumber_count = oddNumber_count + 1
# print("Even number count:" +evenNumber_count)
# print("Odd number count:" +oddNumber_count)

negativeNumber_count = 0
positiveNumber_count = 0
zeroNumber_count = 0
for x in range(5):
    number = int(input("Enter the number."))
    if number==0:
        zeroNumber_count = zeroNumber_count + 1
    elif number > 0:
        positiveNumber_count = positiveNumber_count + 1
    else:
        negativeNumber_count = negativeNumber_count + 1
print("Zero number count",zeroNumber_count)
print("Positive number count",positiveNumber_count)
print("Negative number count",negativeNumber_count)         

