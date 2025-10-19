#Q1 counting positive numbers-------
#problem:given a list of numbers,count how many are positive
#numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

# numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count=0
# for num in numbers:
#     if num>0:
#        positive_number_count+=1
# print("postive numbers are",positive_number_count)

#Q2 sum of even numbers----
#problem:calculate the sum of even numbers up to a given number n
# n=11
# sum_even=0
# for i in range(1,n):
#     if i%2==0:
#         sum_even=sum_even+i
# print("sum of even no up to ",n,"is",sum_even)
        
# #positions count----
# n=10
# position_count=0
# for i in range(1,n+1):
#     if i%2==0:
#         position_count=position_coun0t+1
# print("sum of positions from 1 to",n,"is",position_count)
# 
# Q3  Multiplication table printer----
# table=3
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i*table)

# #Q4  reverse a string using loop------
# str="python"
# reversed_str=""

# for char in str:
#     reversed_str = char+reversed_str    #yaha daba mai variable nicha se dalata hai isliya ulta ho jata hai 
# print(reversed_str)

#Q5 find the first non repated string-----

# input_str="teeteracdacd"

# for char in input_str:
#     if input_str.count(char)==1:
#         print("char is ",char)
#         break

#Q6 Factorial calculator
#problem:compute the factorial of a number using a while loop
# number=5
# factorial=1

# while number>0:
#     factorial=factorial*number
#     number=number-1

# print("factorial value is",factorial)

#Q7 Validate input
#keep asking the user for input until they enter a number between 1 to 10

# while True:
#     number=int(input("enter a number b/w 1 to 10:"))
#     if 1<=number<=10:
#         print("thanks")
#         break
#     else:
#         print("invalid number try again")

#Q8 prime number checker
# number=29

# is_prime=True

# if number>1:
#     for i in range(2,number):
#         if (number%i)==0:
#             is_prime==False
#             break

# print(is_prime)


#Q9 list uniqueness checker 
#problem:check if all the elements in a list are unique.if a duplicate is found,exit the loop and print the duplicate

# items=["apple","banana","orange","apple","mango"]

# unique_item=set()

# for item in items:
#     if item in unique_item:
#         print("duplicate:",item)
#         break
#     unique_item.add(item)

#Q10 Exponential backoff
#problem:Implement an exponential backoff that doubles the wait time b/w retries,starting,from 1 second,but stop after 5 retries
# import time

# wait_time=1
# max_retries=5
# attempts=0

# while attempts< max_retries:
#     print("attempt",attempts+1,"-wait time",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempts+=1
