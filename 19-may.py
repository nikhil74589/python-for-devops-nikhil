# What is function in python.
#1.Every function has their own purpose.
#2.Function is block of instruction(code) which execute inside its own block,
#3.Function is reusable means define one time use manytime (DRY).
#4.Function has two main part first functions defination second function calling.

# How define function in python.
# def add () :
#     a=20
#     b=10
#     c=a+b
#     print(c)
# add()    

# Function divide into 4 category.

# 1. Take nothing return nothing.
# 2. Take nothing return something.
# 3. Take something return nothing
# 4. Take somehing return something.
# 5. In python by default function return NONE .

#Parameters (para) and arguments (args).
#Positional parameter/arguments

# def add (a,b) :
#     c=a+b
#     print(c)
# add(10,20)  
# add(100,200)

# def add (a,b,d) :
#     c=a+b+d
#     print(c)
# add(10,20,30)  

# def table_print(n):
#     for i in range (1,11):
#         print(f"{n} x {i} = {n*i}")
# table_print(1)
# print("-"*20)
# table_print(2)
# print("-"*20)        


#Default parameter

# def add (a=0,b=0) :
#     c=a+b
#     print(c)
# add(10,20,) 
# add(11,22,) 

# def add (a=0,b=0) :
#     c=a-b
#     print(c)
# add(20,10,) 
# add(22,11,)

# def add (a=0,b=0) :
#     c=a*b
#     print(c)
# add(20,10,) 
# add(22,11,)

# def add (a=0,b=0) :
#     c=a/b
#     print(c)
# add(20,10,) 
# add(22,11,)


# def add (a=0,b=0) :
#     print("Addition :", a+b)

# def sub (a=0,b=0) :
#     print("Subtraction :", a-b)    

# def mul (a=0,b=0) :
#     print("Multiplication :", a*b) 

# def division (a=0,b=0) :
#     print("Division :", a/b)   



# num1=int(input("Enter number 1 :")) 
# num2=int(input("Enter number 2 :")) 
# opt=input("Choose option : +, - , * , / : ")
# if opt =="+":
#     add(num1,num2)
# elif opt =="-":
#      sub(num1,num2)
# elif opt =="*":
#      mul(num1,num2)
# elif opt =="/":
#      division(num1,num2)
# else :
#     print("Accurate Input")                 



# For repetative task 

# def add (a=0,b=0) :
#     print("Addition :", a+b)

# def sub (a=0,b=0) :
#     print("Subtraction :", a-b)    

# def mul (a=0,b=0) :
#     print("Multiplication :", a*b) 

# def division (a=0,b=0) :
#     print("Division :", a/b)   

# while True:

#       num1=int(input("Enter number 1 :")) 
#       num2=int(input("Enter number 2 :")) 
#       opt=input("Choose option : +, - , * , / (0: for stop program): ")
#       if opt =="+":
#          add(num1,num2)
#       elif opt =="-":
#            sub(num1,num2)
#       elif opt =="*":
#           mul(num1,num2)
#       elif opt =="/":
#           division(num1,num2)
#       elif opt =="0": 
#           break   
#       else :
#         print("Accurate Input is not given")                 



# def add(a,b):
#     c=a+b
#     return c
# res=add(2,3)
# print(res)

# def add(a,b):
#     return a+b
# res=add(2,3)
# print(res)

# def add(a,b):
#     return "Nikhil"
# res=add(2,3)
# print(res)    


# def add(a,b):
#     return a+b
# res=add(10,30)    

# def sub(a,c):
#     return c-a
# print (sub(10,res))

# def greet(a):
#     return a
# greet("Hello")

# def user_name(a):
#     return a
# user_name("Nikhil")

# print (greet("Hello"),user_name("Nikhil"))


# Practice 

# waf to check number pass by argument is odd or even

# def odd_even(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")
# odd_even(5)        


# Waf to check which number is greater and two number by user

# def check_number(n1,n2):
#     if n1>n2 :
#         print("n1 is greater")
#     else:
#         print("n2 is grater")
# check_number(7,10)         


# Waf to check the character pass by user is vowel or consonanat.

# def check_char(c):
#     if c in "aeiouAEIOU":
#      print(f"This is vowel {c}")
#     else:
#      print(f"this is consonant {c}")
# check_char("n")

# def check_char(c):
#     if c in "aeiouAEIOU":
#      print(f"Char  is  {c} vowel")
#     else:
#      print(f"this is consonant {c}")
# check_char("n")

# user_input="k"
# check_char(user_input)


# Waf to check is number completly divide by 2 and 3 and return

# "Yes number is completly divide"
# "No number is not completly divide"
# def check_number(n):
#     if n%2 ==0 and n%3==0 :
#      print("Yes number is completly divide")
#     else:
#        print("No number is not completly divide")
# check_number(6)

# def check_number(n):
#     if n%2 ==0 and n%3==0 :
#      return "Yes number is completly divide"
#     else:
#        return "No number is not completly divide"
# res=check_number(9)
# print(res)

# Waf to return length of a string pass by user without using len().

# def len_string(s):
#     return len(s)
# print(len_string("python"))

# def len_string(s):
#     c=0
#     for i in s:
#         c=c+1
#     return c  
# print(len_string("python"))

