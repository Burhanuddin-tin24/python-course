
#WRITNG FUNCTION:
# f = open("my.txt", "w")
# print(f.write("I have no enemies!"))
# f.close()

# f = open("my.txt", "r" )
# for line in f:
#    print(f.readline())


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

# class per():
#   def __init__(self, n, a):
#     self.name = n
#     self.age = a
#   def data(self):
#     print(f"the name of the person is {self.name} and age is {self.age} ")

# a= per("burhan", 16)
# b= per("itachi", 16)
# a.data()
# b.data()


# #DECORATORS:
# def decorate(func):
#   def modified():
#     print("here is your answer")
#     func()
#     print("thanks, for using me")
#   return modified
# @decorate
# def calculate():
#   a = int(input("enter number: "))
#   b = int(input("enter number: "))
#   print(a+b)

# calculate()

# #INHERITANCE:
# class student:
#   def __init__(self,name, lastname):
#     self._name= name
#     self._lastname= lastname
#   def show(self):
#     print(f"Incapsulation of student name {self._name} {self._lastname}")

# class teacher(student):
#   def showoft(self):
#     print("levi is added in teacher class with incalsulation")

# s1 = teacher("levi", "ackerman")
# s1.show()
# s1.showoft()

# #CLASS METHODS:
# class person:
#  def __init__(cls, name , age):
#   cls.name = name
#   cls.age = age
   
#  @classmethod
#  def clsmethod(cls, string):
#    return cls(string.split("-")[0], string.split("-")[1])
    
# string = "levi-3000"
# p1 = person.clsmethod(string)
# print(p1.name)
# print(p1.age)

# print(dir(p1))#Shows the methods that can be used on that variable
# print(p1.__setattr__)#Mehtod given by  dir
# print(p1.__dict__)#give the all info about self keyword in class, in dictionary form
# print(help(p1))#Give all the possible information of given variable, like what is happening in the class

#MAGIC AND DUNDER METHODS:
# class employee:
#   def __init__(self, name, role):
#     self.n=name
#     self.r=role
#   def show(self):
#     print(f"Name of the employee is {self.n} and he is a {self.r}")

#   def __len__(self):
#     return len(self.n)#done by dunder method of len

    
# e1= employee("itachi uchiha", "shinobi")
# e1.show()
# print(len(e1))



# #METHOD OVERRIDING:
# class sphere:
#   def __init__(self, x ):
#     self.x =x
    
#   def vol(self): 
#     return (4/3)*3.14*(self.x**3)

# class cone(sphere):
#   def __init__(self,x):
#     self.x=x
#   def volc(self):
#     return(3.14*(self.x**2)*(self.x/3)) + super().vol()#this is where we have do method overriding
    
# sp= sphere(5)
# print("the volume of sphere is" , sp.vol())
# co=cone(5)
# print("the volume of cone is ", co.volc())

# # print(5+5)
# import os
# a= [ a for a in  os.listdir() if a.endswith(".pdf")]
# from PyPDF2 import PdfWriter

# merger = PdfWriter()

# for pdf in a:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()

# #SINGLE AND MULTILEVEL INHERITANCE:

# class animal():
#   def __init__(self, name):
#     self.name = name
#   def speak(self):
#     print("bhau")
    
# class cat(animal):
#   def __init__(self,name):
#     pass
#     # animal.__init__(self,name)
#   def speak(self):
#     return "miauu"

# class cheetah(cat):
#   def __init__(self,breed):
#     self.b=breed
#   def br(self):
#     return f"the breed of the cheetah is {self.b}"
  

# an = cat("dog")
# print(an.speak())
# ca= cat("cat")
# print(ca.speak())
# ch = cheetah( "persian")
# print(ch.br())

#TIME MODULE:
# import time
# def forl():
#     for i in range(5):
#         print(i)
# forl()
# print(time.time())
# print("this is instant")
# time.sleep(5)
# print("this is after delay of 5 secs")

# t  = time.localtime()
# formated = time.strftime("%Y-%m-%D %H:%M:%S", t)
# print(f" current time:  {formated}")
  
#WALRUS OPERATIOR ":=" :
# a = True
# print(a)

#WITH WALRUS...
# print(a:= False)
# food = list()
# while (foods:= input("what food do you like to eat??: ")) != "quit":
#     food.append(foods)
# print(f"here is your list- {food}")

#WITHOUT WALRUS...
# food1= list()
# while True:
#   food= input("what food do you like??: ")
#   if food == "quit":
#     break
#   food1.append(food)
# print(food1)

#SHUTIL MODULE:
# import shutil
# import os
# shutil.copy2("sh.txt", "main2.py")
# shutil.move("merger/sh.txt", "read.md")
#os.mkdir("shutiltest")

#TEXT TO SPEECH:
# import pyttsx3  
# # initialize Text-to-speech engine  
# engine = pyttsx3.init()  
# # convert this text to speech  
# text = "chutiye" 
# engine.setProperty("rate", 10)  
# engine.say(text) 
  
# # play the speech  
# engine.runAndWait()

#REQUESTS MODULE:
# import requests as rq
# from bs4 import BeautifulSoup 

# re = rq.get("https://www.mentalhelp.net/internet/adult-content/")
# # print(re.text)
# soup = BeautifulSoup(re.text, "html.parser")
# # print(soup.prettify)
# for div in soup.find_all("script"):
#     print(div.text)

#CALENDAR MODULE:
# from calendar import *
# year = int(input("enter the year: "))
# print(calendar(year))

import pyttsx3 as py
voice = py.init()
text= "hello!"
voice.setProperty("rate",100)
voice.say(text)
voice.runAndWait()