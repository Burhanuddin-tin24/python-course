# #DATA TYPES:

# #STRINGS: which are enclosd in double quotes
# a = "hello world!"
# #STRINGS METHOD

# a = "my name is burhanuddin"
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.casefold())
# print(a.encode())
# print(a.center(50))
# print(a.endswith("!"))
# print(a.expandtabs())

# #LIST: enclosed in square brackets
# l = [1, 2, 3, 4]
# print(l, type(l))

#  # LIST METHODS
# l = [2,1,6,4,5,6,8,9,4]
# print(l)
# l.append(3)
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# print(l.index(2))
# print(l.count(4))

# #TUPLES
# t = (1, 2, 3, 4)
# print(t, type(t))

# #SETS
# s = {1, 2, 3, 4}
# print(s, type(s))

# #DICTIONARY
# d = {"itachi": "uchiha",
# "shishui": "uchiha",
#     "madara": "uchiha"}

# print(d)


# name = ["thors, thorsfinn, askeladd"]
# for i in name:
#   print(i)

# a = 10
# while (a<0):
#   print(a)
#   a= a-1

# else:
#   print("outside the loop")

# for i in range(1, 21):
#   print("2 x", i, "=", i * 2)
#   if (i == 9):
#     break

# print("this is it!")

# def sum(a,b):
#   sum= a+b
#   print(sum)

# sum(2,4)
# sum(3,6)
# sum(4,6,)

# #f strings
# b= "india"
# a= "burhan"
# print(f"my name is {a} and im from {b}")

# #DOC STRINGS
# def sum(a,b):
#   '''take the number a and b and add them'''
#   sum= a + b
#   print(sum)

# sum(10, 20)
# print(sum.__doc__)

# #RECURSION

# def factorial(n):
#   if (n == 0 or n == 1):
#     return 1
#   else:
#     return n * factorial(n - 1)

# print(factorial(8))

# def multiply(x):
#   if x == 10:
#     return
#   else:
#     print(x)
#     return multiply(x + 1)

# multiply(2)

# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)

# def sum_of_integers(n):
#     # Base case: When n is 1, return 1 (the sum of the integers from 1 to 1).
#     if n == 1:
#         return 1
#     # Recursive case: Sum the current number (n) with the sum of integers from 1 to (n-1).
#     else:
#         return n + sum_of_integers(n - 1)

# print(sum_of_integers(99))
# print(fibonacci(3))

# # FOR AND WHILE LOOPS WITH ELSE:
# # for i in range(10):
# #   print(i)

# # else:
# #   print("sorry no i ")

# i = 0
# while i<6:
#   print(i)
#   i = i+1

# else:
#   print("no i ")

# #EXCEPTION HANDLING:
# a = input("enter the number: ")
# print(f"the multiplication table of {a} is:")
# try:

#  for i in range(1,11):
#   print(f"{a} x {i} =  {int(a)*i}")
# except:
#    print("invalid input")

# print("this code is working")

# #CUSTOM ERROR:
# a = (input("enter the  'q' QUIT: "))
# if (a != "q"):
#   raise ValueError("invalid input")
# print(a)

# import random as rd
# # print(rd.random())

# a = int(input("guess the computer number:- "))
# b = rd.randrange(1,101)
# if a>b:
#   print("your number is", a)
#   print("computer number is ", b )
# elif a<b:
#   print("your number is ", a)
#   print("computer number is", b)

# else:
#   print("your number is ", a)
#   print("computer number is", b)

# #ENUMERATE:
# list = [29,39,10,45,17]
# for index, list in enumerate(list):
#   print(list)
#   if(index==3):
#     print("you have top")


# #GLOBAL AND LOCAL VARIABLE:

# a=10
# print(a)
# def func():
#   global a
#   a = 15
#   b =10
#   a = 20
#   print(a+b+a)

# print(f"by using the global keyword your global variable is changed to {a}")
# func()


# # CALCULATOR
# while True:

#   n1 = int(input("enter your number: "))
#   n2 = int(input("enter second your number: "))
#   print("press a for additon")
#   print ("press s for subtraction")
#   print ("press m for multiplication")
#   print ("press d for division")
#   print("-->press q for quit")
#   opr = input("enter your opertion: ")

#   if opr=="a":
#     print(n1+n2)

#   elif opr=="s":
#     print(n2-n1)

#   elif opr=="m":
#     print(n1*n2)

#   elif opr=="d":
#     print(n1/n2)

#   elif opr=="q":
#     break

#   x= input("press c for continue or press q for quit")
#   print(x)
#   if x=="q":
#     break

# def sumofodd(n):
#   return sumofodd(n+2)

# print(sumofodd(1))
