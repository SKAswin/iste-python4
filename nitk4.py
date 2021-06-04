# problrm1
# class car:
#
#     def __init__(self,model,name,year,color,horsepower):
#         self.model=model
#         self.name=name
#         self.year=year
#         self.color=color
#         self.horsepower=horsepower
#         print("car class is created")
#
#     def selfdescription(self):
#         print("the description of the car is following")
#         print("model:",self.model,"\n","name:",self.name,"\n","year:",self.year,"\n",
#               "color:",self.color,"\n","horsepower",self.horsepower)
#
#     def changename(self, name):
#         self.name=name
#         print("the changed name",self.name)
#
#     # def changeddescription(self):
#     #     print("color:",self.color)
#
#     def changecolor(self,color):
#         self.color=color
#         print("the changed color",self.color)
#
#     def __del__(self):
#         print("destructor called,car deleted")
# #
# c=car("F1","Ferrari SF90","2019","red","1000")
# c.selfdescription()
# c.changecolor("blue")
# # c.selfdescription()
# # c.changeddescription()
# # if we want only the car color changed only to print we can do this way
# c.changename("red bull")
# # c.selfdescription()
# del c

# problem2
# import random
# n1=input("what is your input\n")
# b=[]
# # n1="aswin"
# for i in range(0,len(n1),3):
#     b.append(n1[i:i+3])
# print(b)
# d=""
# while(b!=[]):
#     c=random.choice(b)
#     b.remove(c)
#     d=d+c
# print(d)

# problem 3
# class students:
#     def __init__(self,rollno,phoneno,grade):
#         self.rollno=rollno
#         self.phoneno=phoneno
#         self.grade=grade
#         print("class is created")
#
#     def selfdescription(self):
#         print("the attributes of the student are\nrollno:",self.rollno,"\nphoneno:",self.phoneno,"\ngrade:",self.grade)
#
#     def phonenochange(self,phoneno):
#         self.phoneno=phoneno
#         print("the changed phoneno is",self.phoneno)
#
#
# class sports(students):
#     def __init__(self,sports):
#         self.sports=sports
#         print("sports class is created")
#
#     def sportsdescription(self):
#         print("the sport the student play is",self.sports)
#
#     def sportchange(self,sportchange):
#         self.sportchange=sportchange
#         print("the changed sport is",self.sportchange)
#
#     def __del__(self):
#         print("the student don't play any sports")
#
# s=students("201MT053","9063584208","btech1 year")
# s.selfdescription()
# sp=sports("cricket")
# sp.sportsdescription()
# s.phonenochange("8712706625")
# s.selfdescription()
# sp.sportchange("volleyball")
# del sp
