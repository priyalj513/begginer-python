# def is_prime(n):
#     if n<=1:     #1 aur negative numbers prime nhi hota
#         return False
#     for i in range(2,n):#agar kissi number se divide ho jata hai to prime number nhi hai
#         if n%i==0:
#             return False
#     return True

# print(is_prime(7))
# print(is_prime(4))

# x=str(3)
# y=int(4)
# z=float(5)
# print(x,y,z)

# #check type
# x=5
# y="hello"
# print(type(x))
# print(type(y))

# x,y,z="orange","green","red"
# print(x,y,z)
# x=y=z="orange"
# print(x,y,z)

# #unpacking
# fruits=['apple','banana','cherry']
# x,y,z=fruits
# print(x,"",y,"",z)

#global variable -- 0 avariable that are created outside of a function
# x="awesome"

# def my_func():
#     print(x)

# my_func()

# x="awesome"

# def my_func():
#     x="fantastic"
#     print("the value of:",x)

# my_func()
# print("the value of:",x)

#treat create global variable inside func
# def my_funct():
#     global x
#     x="fantastic"
#     print(x)

# my_funct()
# print(x)

# x=b'hello'
# print(type(x))

#convert from one type to another
# x=1
# y=2.8
# z=3j
# x=float(x)
# print(x)
# print(type(x))

#python does not have random() function to make a random number so python have a module called random module
# import random

# for i in range(random.randrange(2,10)):
#     print(i)

# import random

# for i in range(5):
#     print(random.randrange(2,10))

a="hello World!"
print(a.strip())
print(a.split(","))

