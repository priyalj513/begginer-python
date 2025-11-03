#print value ko bhar nhi bhejta function ka 
# def add(a, b):
#     print(a + b)

# result = add(5, 3)
# print("Result is:", result)     #idhar output 8 or none aaiga kyki call kara print kiya hai yaha print mai to kuch
#hai hi nhi matlab variable ka dabbba mai to kuch hai hi nhi internally 

#or return directly daba ki andar ki value ko return karta hai or terminate kar deta hai like
# def add(a, b):
#     return(a + b)

# result = add(5, 3)
# print("Result is:", result)  

#Q1 basic fuction syntax
# def square(number):
#     return (number**2)

# print(square(4))


#Q2 Function with multiple parameters
#Create a function that takes two numbers as parameters and returns their sum.
# def add(num1,num2):
#     return num1+num2

# result=add(2,3)
# print(result)



#Q3 polymorphism in functions
#problem:Write a function multiply that multiplies two numbers,but can also accept and multiply strings
# def multiply(p1,p2):
#     return p1*p2

# print(multiply(2,3))
# print(multiply("a",5))

#Q4 Function returning multiple values
#Problem:create a function that returns both the area and circumference of a circle given its radius
# import math
# def circle_area_circum(r):
#      area=math.pi*r**2
#      circumference=2*math.pi*r
#      return area,circumference

# result=circle_area_circum(2)
# print("a=",area,"c=",circumference)
#Q5 Default parameter value
#Problem:Write a function that greets a a user.if no name is provided,it should greet with a default name
# def greet(name = "user"):    #idhar hum parameter ko as a variabl treat kar rha hai 
#     return "hello, " +name + "!"

# print(greet())
# print(greet("chai"))

#Q6 Lambda Function 
#Problem:create a lambda function to computer the code of a number


# cube=lambda x:x**3
# print(cube(3))

#Q7 function with args
#Problem:write a function that takes variable number of arguments and return their sum
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4))

#Q8Function with **kwargs
#Problem:Create a function that accepts any no of keyword arguments and prints them in the form of key:value
