
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


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample blog post data
posts = [
    {
        'id': 1,
        'title': 'Introduction to Flask',
        'content': 'Flask is a micro web framework for Python.',
    },
    {
        'id': 2,
        'title': 'Getting Started with Flask',
        'content': 'Learn the basics of creating web applications with Flask.',
    },
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return 'Post not found', 404

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {
            'id': len(posts) + 1,
            'title': title,
            'content': content,
        }
        posts.append(new_post)
        return redirect(url_for('home'))

    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
