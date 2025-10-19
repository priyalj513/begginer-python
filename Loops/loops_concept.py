# count=1
# while count<=5:
#     print("hello")
#     count+=1

# i=1
# while i<=100:
#     print("apnacollege")
#     i+=1

#print numbers from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i=i+1

#print numbers from 5 to 1
# i=5
# while i>=1:
#     print(i)
#     i-=1

# print("Loop ended")

#Q1 print numbers from 1 to 100
# num=1
# while num<=100:
#     print(num)
#     num+=1

#Q2 print numbers from 100 to 1
# num=100
# while num>=1:
#     print(num)
#     num=num-1
#Q3 print the table of 10
# n=int(input("enter number: "))
# i=1
# # tab_num=3
# while i<=10:
#     print(i*n)
#     i+=1

#q4 print the given list by using while loop 
# nums=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while index<=len(nums)-1:
#     print(nums[index])   #here it means nums[0],num[1],num[2]
#     index+=1

#practice example
# city=["jaipur","delhi","pune","banglore"]
# index=0
# while index<len(city):
#     print(city[index])
#     index+=1

#search for a number x in this tuple using loop

# tup=(1,4,9,16,25,36,49,64,81,100)
# index=0
# x=36
# while index<len(tup):
#     # print(tup[index])
#     if tup[index]==x:
#         print("found at index",index)
#         break
#     else:
#         print("finding")
    # index+=1

# i=1
# while i<=5:
#     if (i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

#for Loop are used for sequential traversal
# list=[1,2,3]
# for el in list:
#     print(el)

# veggies=["potato","brinjal","ladyfinger","cucumber"]

# for val in veggies:
#     print(val)

# tup=(1,2,3,4,2,8,9)

# for num in tup:
#     print(num)

# str="apnacollege"

# for char in str:
#     if(char=="o"):
#       print("o found")
#       break
#     print(char)
# else:
#    print("end")

#Question using for loop
#Q1 print the elements of the following list uding a loop
# list=[1,4,9,16,25,36,49,64,81,100]

# for i in list:
#     print(i)

#Q2 search for a number x in this tuple using loop:
# nums=(1,4,9,16,25,36,49,64,81,100,49)
# x=49

# idx=0
# for el in nums:
#     if(el==x):
#       print("number found at idx",idx)
#       break
#     idx +=1

# seq=range(5)
# for i in range(10):
#     print(i)

# for i in range(2,10,2):  #range(start,stop)
#     print(i)

# for i in range(2,100,2):
#     print(i)

#practice Que for range 
#Q1 print number from 1 to 100 
# for var in range(1,101):
#     print(var)

#Q2 print numbers from 100 to 1
# for i in range(100,0,-1):
#     print(i)

#Q3 print the multiplication table of number n lets say 2
# n=int(input("enter number: "))
# for i in range(1,11):
#     print(n*i)

#pass statement---------
# for i in range(5):
#     pass
# if i>5:
#     pass

# print("some useful work")

#Practice--------
#Q1 WAp to find sum of first n numbers
# n=6
# sum=0
# for i in range(1,n):
#     sum+=i

# print("total sum is ",sum)
# n=7
# sum=0
# i=1
# while i<=7:
#     sum+=i
#     i+=1
# print(sum)

#WAP to find factorial of first n numbers(using for)
n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1

print("factorial=",fact)
