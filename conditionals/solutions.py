#  Q1 age group categorization
#Classify a person's age group:Child(<13),Teenager(13-19),Adult(20-59),Senior(60+).
# age=int(input("enter the age: "))
# if age<13:
#     print("child")
# elif age<20:
#     print('teenager')
# elif age<60:
#     print("adult")
# else:
#     print("senior")
# Q2 Movie tickets pricing
#problem: Movie tickets are based on age:$12 for adults(18 and over),$8 for children.Everyone gets $2 dollar on wednesday
# age = int(input("enter age: "))
# day=input("enter day: ")
# price=12 if age>=18 else 8

# if day == "wednesday":
#     price=price-2

# print("Ticket price for you is $",price)

# #Q3 Grade Calculator
# #problem:Assign a letter Grade based on a students score:A(90-100),B(80-89),C(70-79),D(60-69),F
# score=int(input("enter student score: "))

# if score>=101:
#     print("please verify your grade again ")
#     exit()
    
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("Fail")

# Q4 fruit ripenese checker
#Problem:determine if a fruit is ripe,overripe,or unique based on its colour
#(e.g Banana:green-unripe,yellow-ripe,brown-overripe)
# fruit="banana"
# color="yellow"
# if fruit=="banana":
#     if color == "green":
#         print("unripe")
#     elif color == "yellow":
#         print("ripe")
#     elif color == "brown":
#         print("overripe")
#     else:
#         print("unique color")
# else:
#     print("fruit is not listed here: ")

# print(fruit,"is",color)

#Q5 Weather activity suggestion
#problem:suggest an activity based on weather
#(eg sunny-go for walk,rainy-read a book,snowy-build a snowman)
# weather=input("suggest a weather: ")
# if weather=="sunny":
#     print("go for walk")
# elif weather=="rainy":
#     print("Read a book")  
# elif weather == "snowy":
#     print("build a snowman")


#Q6 Transportation mode selection 
#Problem:Choose a mode of transportation based on the distance
# (e.g<3km: walk,3-15km:bike,>15=car)

# distance=int(input("distance= "))
# if distance<=3:
#     transport="Walk"
# elif distance<=15:
#     transport="bike"
# else:
#     transport="car"
   
# print("Ai recommend you the transport of " , transport)

# Q7 coffee customization
# problem:Customize a coffe order:
# "Small","Medium", or "large" with an option for "extra soft" of expresso.

# coffee_size=input("Ask the cofee size: ")
# extra_shot=input("do you want extra shot ")

# if extra_shot == "yes":
#     print(coffee_size + " coffee with an extra shot")
# else:
#     print(coffee_size+ " coffee")

#Q8 password strength checker
#problem:check if a password is "weak","medium",or "strong".
# Criteria:<6 chars(weak),6-10 chars(medium),>10 chars(strong)

# password="secure3@pass"

# if len(password)<6:
#     strength="weak"
# elif len(password)<=10:
#     strength="medium"
# else:
#     strength="strong"
# print("password is ", strength)

# #Q9 Leap year checker
# # problem:determine if a year is leap year.(Leap years are divisible by 4,but not by 100 unless also div by 400)

# year=int(input("enter year: "))

# if year%400==0 or (year%4==0 and year%100 !=0):
#    print(year,"is a leap year")
# else:
#   print(year,"is not a leap year")


#Q10 Food recommendation
#Recommend a type of pet food based on the pet's species and age 
#(e.g dog<2 years-puppyfood,cat>5 years-senior cat-senior cat food)
species=input("enter pet species: ")
age=int(input("enter pet age in years: "))

if species=="dog":
    if age<=2:
        print("Recommended food:puppy food")
    elif age>=5:
        print("Recommended food : adult dog food: ")
    else:
        print("senior dog food: ")
elif species=="cat":
    if age<5:
        ("kitten food")
    elif age>=5:
        ("adult cat food")
    else:
        ("senior cat food")
else:
    print("sorry,food recommendatio not available for this species")
