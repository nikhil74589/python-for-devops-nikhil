# while loop :
# initaializer
# condition
# increment/decrement
    
# i=1
# while i<=10 :
#     print(i)
#     i+=1

# wap to print only even number from 10 to 20
# start=10
# end=20
# while start <= end:
#     if start%2==0:
#         print(start)
#     start+=3



# wap to print the total of even number from 1 to 15.
# i = 1
# total = 0

# while i <= 15:
#     if i % 2 == 0:
#         total = total + i
#     i = i + 1

# wap to check the given string by user is "palindrome or not palindrome "

# text="16461"
# copy_text=text
# rev=""
# i=len(text)-1

# while i>=0:
#     rev=rev+text[i]
#     i-=1
# if copy_text==rev:
#     print("palindrome")
# else:
#     print("not palindrome")    


# text="16451"
# copy_text=text
# rev=""
# i=len(text)-1

# while i>=0:
#     rev=rev+text[i]
#     i-=1
# if copy_text==rev:
#     print("palindrome")
# else:
#     print("not palindrome")  

# wap to reverse the digit :1234 otput : 4321  
       
# num = 1234
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number is:", reverse)



# 18 May 2026
# 18 May 2026
# 18 May 2026
# 18 May 2026

# wap to count total number of vowels in a string using while loop.
# str1="Rohan"
# size=len(str1) -1
# while size>=0:
#     print(size)
#     size-=1

# str1="Rohan"
# size=len(str1) -1
# n=0
# while n<=size:
#     print(size)
#     size-=1

# str1="Rohan"
# size=len(str1) -1
# n=0
# cv=0
# while n<=size:
#     # print(str1[n])
#     if str1[n] in "aeiou":
#         cv+=1
#     n+=1    
# print(cv)


# str1="Rohan"
# size=len(str1) -1
# n=0
# cv=0
# cc=0
# while n<=size:
#     # print(str1[n])
#     if str1 [n] in "aeiou":
#         cv+=1
#     else:
#         cc+=1

#     n+=1    
# print("Total Vowels =", cv)
# print("Total Consonants =", cc)

# WAP to print formatted table on a number given by user using while loop

# num = int(input("Enter a number: "))
# i = 1
# print("\nFormatted Table of", num)
# print("-------------------------")

# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1

#  WAP to print formatted table on a number given by user using while loop

user_num=6
i=1
while i<=10:
    print(f"{user_num} * {i} = {user_num *i}")
    i+=1