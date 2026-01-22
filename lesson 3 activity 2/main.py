height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 20:
    print("You are underweight.")
elif BMI <= 33:
    print("You are healthy.")
elif BMI <= 36:
    print("You are over weight.")
elif BMI <= 40.8:
    print("You are severely over weight.")
elif BMI <= 50.9:
    print("You are obese.")
else:
    print("You are severely obese.")