# lets make a calculator 
def add(e,f):
    return e+f
def subtract(e,f):
    return e-f
def multiply(e,f):
    return e*f
def divide(e,f):
    return e/f

num1=int(input("enter your first no. to calculate"))
num2=int(input("enter your second no. to get the answer"))

print("sum:",add(num1,num2))
print("difference:",subtract(num1,num2))
print("product:",multiply(num1,num2))
print("quotient:",divide(num1,num2))