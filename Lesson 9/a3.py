print("HCF of twoo numbers")
n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
while n2!=0:
    temp=n2
    n2=n1%n2
    n1=temp

print("HCF is: ",n1)