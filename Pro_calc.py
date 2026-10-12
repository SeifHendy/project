def addition(x,y):
    print(x+y)
def substraction(x,y):
    print(x-y)
def multi(x,y):
    print(x*y)
def division(x,y):
    print(x/y)
operation = input("please enter the operation: ")
x=int(input("enter first number: "))
y=int(input("enter second number: "))
if operation == '+':
    addition(x,y)
elif operation == '-':
    substraction(x,y)
elif operation == '*':
    multi(x,y)
elif operation == '/':
    division(x,y)
else:
    print("try again")