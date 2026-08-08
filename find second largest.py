# second largest
n=int(input("how many number you want to enter : "))
number=[]
for i in range(n):
   num=int(input("enter the number : "))
   number.append(num)
print("the numbers you enterd are: ",number)
number.sort()
print("the sorted number from ascending to decending order are : ",number)   
print("the second largest number is ",number[-2])