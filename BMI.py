weight=float(input("enter your weight"))
height=float(input("enter your height"))
BMI=(weight/height**2)
print(BMI)
if BMI < 18.5:
    print("under weight")
elif BMI > 18.4 and BMI < 25:
    print("normal") 
elif BMI > 24.9 and BMI < 40:
    print("overweight")
else:
    print("obese")