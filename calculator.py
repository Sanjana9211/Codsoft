#SIMPLE CALCULATOR

print("SIMPLE CALCULATOR")

n1=int(input("Enter the first number : "))
op=input("Enter the operation (+,-,*,/) : ")
n2=int(input("Enter the second number : "))

if op=='+':
    print(f"{n1} + {n2} = {n1+n2}")
elif op=='-':
    print(f"{n1} - {n2} = {n1-n2}")
elif op=='*':
    print(f"{n1} * {n2} = {n1*n2}")
elif op=='/':
    if n2==0:
        print("Division not possible...")
    else:
        print(f"{n1} / {n2} = {n1/n2}")
else:
    print("Not a valid operation")