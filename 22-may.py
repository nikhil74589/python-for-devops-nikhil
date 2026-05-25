#Waf to check how many vowel in a given string.
# def vowel_count(n):
#     c=0
#     for i in n:
#         if i in "aeiou":
#          c+=1
#     return c    
# res =vowel_count("infrastructure")
# print(res)

# Local variable vs global variable 

# name="Nikhil" #global variable
# def masg():
#     #global name
#     name="Nikhil" #Local variable
#     print("Inside:",name)
# msg()
# print("Outside:",name)    

# Waf to count char "p" in "python programming" return total occurence.

# def char_count(dest,find):
#     c=0
#     for i in dest:
#         if i == "find":
#          c+=1
#     return c

# dest=("python programming") 
# find="p"
# res=char_count(dest,find) 
# print(res)

# Waf to return sum of strings indexes.

# "python"
# def sum_of_indexes(n):
#      s=0
#      for i in range (len(n)):
#         s=s+i
#      return s 
# res=sum_of_indexes("python")  
# print(res)