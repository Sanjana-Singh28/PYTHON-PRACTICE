# taking input by own

# list1=[1,2,3,4,5,6]
# last=list1.pop()
# list1.insert(0,last)
# print("rotated list is :",list1)

# easyway

list=[1,2,3,4,5,6]
result=[list[-1]] + list[:-1]
print("the rotated list is :",result)