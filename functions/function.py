# # def my_function():
# #     print("hello from a function")

# # my_function()
# # my_function()

# #without functions
# temp1=77
# celsius1=(temp1-32)*5/9
# print(celsius1)

# temp2=95
# celsius2=(temp2-32)*5/9
# print(celsius2)

# temp3=50
# celsius3=(temp3-32)*5/9
# print(celsius3)

#start functions here 
# def calc_sum(a,b):  #here a and b are parameters
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(5,10)
# calc_sum(2,17)

# def greetings_function(name,age):   #here name is the parameter
#     print('welcome',name,"you are ",str(age),"year old")

# greetings_function('john',27)     #here john is argument

# #agar hum ismai integer pass karta hai
# def greetings_function(name):
#     print('welcome',str(name))   #to yaha directly convert aisa karta hai 

# greetings_function(34)


#-------when we dont know how much parameters have to passs then we use *(asterisk)
# def func(*names):
#     print("welcome",names[1])

# func('priya','anu','tanu')


#agr hum directly define karta hai parameter and argument
# def greetings_function(name,age):
#     print('welcome',name,'you are',str(age),'year old')

# greetings_function(name='john',age=20)

#with input
# def greetings_function(name,age):
#     print('welcome',name,'you are',age,'year old')

# name=input("enter your name: ")
# age=input("enter your age: ")
# greetings_function(name,age)



#return statement 
# def add_numbers(num1,num2):
#     return num1+num2

# sum=add_numbers(2,3)
# print(sum)

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit-32)*5/9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))


# def get_greeting():
#     return "hello from a function"

# message=get_greeting()
# print(message)

# print(get_greeting())

# def my_func(name):
#     print("hello",name)

# my_func("priyal")

# def my_func(f_name,l_name):
#     print(f_name,l_name)

# my_func("priyal","jain")


# def my_func(name="priyal"):g
#     print("hello",name)

# my_func("nisha")
# my_func("teena")
# my_func("myra")
# my_func()

#send arguments with key value syntax they are called keyword argument
# def my_func(animal,name):
#     print("i have a ",animal)
#     print("my",animal,"name is ",name)

# my_func(animal="dog",name="bobby")

# #positional argument
# def my_function(animal,name):
#     print("i have a ",animal)
#     print("my",animal,"name is",name)

# my_function("dog","buddy")

# #mixing positional and keyword arguments
# def my_animal(animal,name,age):
#     print("i have a",age,"year old",animal,"named",name)

# my_animal("dog",name="buddy",age=5)

#passing diff datatype
# def my_func(fruits):
#   for i in fruits:
#     print(i)

# my_fruits=["apple","banana","orange"]
# my_func(my_fruits)

#returning diff data types
# def my_fun():
#     return (["apple","banana","orange"])

# fruits=my_fun()
# print(fruits[0])

#arbitrary arguments-*args(for any no of parameters)
# def my_func(*kids):
#     print("the youngest child is",kids[2])

# my_func("priya","tanu","sonu")

#arbitrary arguments type ky hoga by default==tuple
# def my_func(*args):
#     print("Type",type(args))
#     print("first arg",args[0])

# my_func("priya","tanu","sonu")


#using *args with regular arguments
# def my_func(greeting,*names):
#     for name in names:
#         print(greeting,name)

# my_func("hello","priya","seema","teena")
  

# mbining *args and **kwargs

# def my_func(tittle,*args,**kargs):
#     print(tittle,args,kargs)

# my_func("family","members","head",memname="priya",headname="pitaji")

# Unpacking Lists with *
# def my_func(a,b,c):
#     return a+b+c

# numbers=[1,2,3]
# result=my_func(*numbers)
# print(result)

#nonlocal func 
def outer():
    x=20
    def inner():
        nonlocal x
        x=10
        print("inner x:",x)

    inner()
    print("outter x:",x)
outer()