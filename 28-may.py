# Slicing.
# marks=[10,20,30,40,50,60,70,80]
# # [start-0:stop-1:step-1]

# sub_list=marks[0:8:2]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80]
# # [start-0:stop-1:step-1]

# sub_list=marks[8:0:-1]
# print(sub_list)

# 6.Traversing.
# marks=[10,20,30,40,50,60,70,80]
# for i in range (len(marks)):
#     if marks[i]%2==0:
#         print(f"This elm is even : {marks[i]}")
#     else:
#         print(f"This elm is odd : {marks[i]}")

# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# for i in marks:
#      if i%2==0:
#           print(f"This elm is even : {i}")
#      else:
#         print(f"This elm is odd : {i}")

# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# total=0
# for i in marks:
#     total=total+i
# print(total) 
   
# Slicing.

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]

# sub_list=marks[5:-1]
# print(sub_list)

#WAP to swap the first value of list with last value of list.
# [10,11,20,31,30,33,40,55,60,70,80]
# # [80,11,20,31,30,33,40,55,60,70,10]


# my_list=[10,20,30,40]

# first_elm=my_list[0]
# last_elm=my_list[-1]

# my_list[-1]=first_elm
# my_list[0]=last_elm

# print(my_list)

# Wap to find the sum of all elemts in the list :[10,20,30,40]

# list=[10,20,30,40]
# total=0
# for i in list:
#     total=total+i
# print(total) 


# wap to find the sum of only even elements in the list :[10,3,4,6,22,31,33,55,40]

# list=[10,3,4,6,22,31,33,55,40]
# sum_even=0
# for i in list:
#     if i% 2==0:
#         sum_even=sum_even+i
# print("Sum of even elements=",sum_even)        


# wap to find the sum of only odd elements in the list :[10,3,4,6,22,31,33,55,40]

# list=[10,3,4,6,22,31,33,55,40]
# sum_odd=0
# for i in list:
#     if i %2 !=0:
#         sum_odd=sum_odd+i
# print("Sum of odd elemts=",sum_odd)        


# wap to find the count of how many int value and how many str in the list

# list =[70,"aman",50,10,20,"rohan","iq-india"]
# int_value=0
# str_value=0
# for i in list:
#    if type (i)==int:
#        int_value=int_value+1 
#    elif type (i)==str:
#        str_value=str_value+1

# print(int_value)
# print(str_value)          