sum=0
n=int(input("enter the number"))
while n>0:
    r=n%10
    n=n//10 #give int //
    sum=sum+r

print("the number is ", int(sum))
