
# #LAMBDA FUNCTIONS:
# y = int(input("enter your number"))
# sum = lambda y: y * 2
# print(sum(y))

# #MAP: it simply map the function with the given data
# l = [1, 2, 3, 4]


# def cube(x):
#   print(x * x * x)


# l2 = list(map(cube, l))
# print()

# # #FILTER: simply it will filter your data according to given conditon
# l = [1, 2, 3, 4, 5, 6, 7]


# def fil(x):
#   return x > 4


# l2 = list(filter(fil, l))
# print(l2)
# print()

# #FILE IO:

# f= open("my.txt", "r")
# # print(f)
# print(f.read())
# f.close()




#VIRTUAL ENVIROMENT:
#first create a new folder, then open that folder in cmd, then write "python -m enev myenv",
#then for actvating it type "foldername\scripts\activate" and install modules with the help of pip.

#OS MODULE: provides many functions to interact with operating system..


#  #INTRODUCTION TO CLASS
# class person:
#   name = "itachi"
#   lastname = "uchiha"
#   occupation = "shinobi"

#   def data(self):
#     print(
#         f"person name is {self.name} {self.lastname} and he is a {self.occupation}."
#     )


# a = person()
# a.data()
# print()

# # if you want to add another person with same characterstics or the same variables you can do that by:
# b = person()
# b.name = "shishui"
# b.lastname = "uchiha"
# b.occupation = "ambu black cops"
# b.data()
# print()

# and you can add more objectss like this.

# #CONSTRUCTOR:

class per():
  def __init__(self, n, a):
    self.name = n
    self.age = a
  def data(self):
    print(f"the name of the person is {self.name} and age is {self.age} ")

a= per("burhan", 16)
b= per("itachi", 16)
a.data()
b.data()

#WRITNG FUNCTION:
# f = open("my.txt", "w")
# print(f.write("I have no enemies!"))
# f.close()

f = open("my.txt", "r" )
for line in f:
   print(f.readline())