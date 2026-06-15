# 1.for loop : ranged based
# 2.while loop : condition based

# 1.for loop 
# range always works with integer number.
# range (start:0 ,stop-1 ,step:1)

# for i in range (10):
#      print("Nikhil")

# for i in range (0,5,1):
#     print(i)

# for i in range (0,5,2):
#     print(i)

# for i in range (0,7,2):
#     print(i)

# for i in range (1,16,1):
#     print(i)

# for i in range (1,16,2):
#     print(i,end = " ")

# for i in range (1,20):
#     if i == 10 :
#         break
#     print (i)

# for i in range (1,20):
#     if i == 10 :
#         continue
#     print (i)

# for i in range (1,20):
#     if i%2 == 0 :
#         print (i,end = " ")

# for i in range (1,21):
#     if i%2 == 0 :
#        print (i,end = " ")

# for i in range (1,21):
#     if i%2 != 0 :
#        print (i,end = " ")

# for i in range (1,21):
#     if i%2 != 0 :
#        print (f"Odd : {i}")
#     else :
#         print(f"Even : {i}")

# for sum
# s=0  
# for i in range (1,5):
#     s = s + i
#     print(s)

# s=1  
# for i in range (1,5):
#     s = s * i
#     print(s)

# s=1  
# for i in range (1,5):
#     s = s * i
# print(s)

# for i in range (10,1,-1):
#     print(i)

# for i in range (10,0,-1):
#     print(i)

# for r in range (10,-3,-1):
#     print(r)





# wap to takes start_point and end_point from user input and print all number divisible by 2 and 3:

# start_point = int(input("Enter start point: "))
# end_point = int(input("Enter end point: "))

# print("Numbers divisible by 2 and 3 are:")

# for num in range(start_point, end_point + 1):
#     if num % 2 == 0 and num % 3 == 0:
#         print(num)



# start = 1 
# end=30
# for num in range (start, end + 1):
#     if num % 2 == 0 and num % 3== 0:
#         print (num)



    
# wap to take a number from user_input and print formated table.
# format :

# num = int(input("Enter the number :"))
# for i in range (1,11) :
#    print (f"{num}*{i} = {num * i}")


# wap to take a number from user_input and print reversed formated table.

# num = int(input("Enter the number :"))
# for i in range (10,0,-1) :
#    print (f"{num}*{i} = {num * i}")