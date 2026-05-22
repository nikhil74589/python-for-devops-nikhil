
#Traversing of string using range ()


# name = "python"
# size = len(name)
# for i in range (size):
#     print (name [i]) 


# name = "python"
# for i in range (len (name)):
#     print (name [i]) 


# without range 

# name = "python"
# for i in name:
#     print (i)


# name = "python"
# size = len(name)
# for i in range (size):
#     print (name)
 
# name = "python programming"
# size = len(name)
# for i in range (size):
#     print (name [0]) 


  
# name = "python programming"
# size = len(name)
# for i in range (size):
#     print (name [-1])

# name = "python"
# size = len (name)
# for i in range (size):
#     print(name[i],name,i)


# name = "python programming"
# size = len(name)
# for i in range (size):
#     print (name [i], i)


# var1="Devops Engineer"
# for i in var1 :
#     if i =="e":
#         continue
#     print (i, end=" ")


# var1="Devops Engineer"
# for i in var1 :
#     if i =="e" or i=="E" :
#         continue
#     print (i, end=" ")    



# wap to count all the vowels from give string : "this is devops batch".

# str1 = "this is devops batch"
# v_count=0
# for i in str1 :
#     if i in "aeiou":
#         print(i,end=" ")
#         v_count+=1
# print(v_count)        

# str1 = "this is devops batch"
# v_count=0
# c_count=0

# for i in str1 :
#     if i in "aeiou":
#         print(i,end=" ")
#         v_count+=1
#     else :
#         c_count+=1  #Assignment operator

# print(v_count) 
# print(c_count)  

# str1 = "this is devops batch"
# v_count=0
# c_count=0

# for i in str1 :

#     if i ==" ":
#         continue

#     if i in "aeiou":
#         print(i)
#         v_count+=1   
#     else :
#         c_count+=1  #Assignment operator

# print("vowel_count =", {v_count}) 
# print("Consonant count =", {c_count}) 


    
# wap to print your name in reverse format.


# name="nikhil"
# rev = ""
# for i in name :
#     print(i)



# name="nikhil"
# rev = ""
# for i in name :
#     rev = i+rev
# print(rev)


# name="PYTHON"
# rev = ""
# for i in name :
#     rev = i+rev
# print(rev)

# name = "PYTHON"
# size = len (name)
# for i in range (size):
#     print(name[i],name,i)

# 13th MAY class

# wap to sum of the indices of a string : "python"
# name = "python"
# size = len(name)
# total_sum = 0
# for i in range (size) :
#     print(f"character :{name[i]},index {i}") 
#     print(f"sum of the indices :{total_sum}")

     
# wap to print the factorial from 1 to 8

# for n in range(1, 9):
#     fact = 1
    
#     for i in range(1, n + 1):
#         fact = fact * i
    
#     print("Factorial of", n, "=", fact)

# wap to print only prime number from 1 to 15

# for num in range(1, 16):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)