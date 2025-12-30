print("Pallindrome number")
n=int(input("Enter a number: "))
reverse=0
temp=n
while temp>0:
    remen=temp%10
    reverse=remen+(reverse*10)
    temp=int(temp/10)

if n==reverse:
    print("The number is a pallindrome")
else:
    print("The number isn't a pallindrome! ")