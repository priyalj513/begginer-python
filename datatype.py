#object types/data types
#numbers

x=2
y=3
z=4
# print(x)
# print(x+y)
# print(x+(y*z))
# print(40+2.23)      #nhi karna chaiya aisa 

# print('chai' + 'code')   #operator overloading hota hai 
# print(x,y,z)   
# print(x+1,y*2)
# print(y%2)
# print(2**1000)       #python ki kasiyat hai big numbers ko calculate kardeta hai vo bhi bilkul shi


# result = 1/3.0
# print(result)

# repr('chai')      #represent is a function that gives the developer freiendly version
#                   ##extra quotos ka sath taki clear pata chale ki yai string hai 
# print(repr)       #yaha print kiya isliya yai likha aa rha hai output main <built-in function repr>
# print(repr('chai'))            #yaha isko call kiya hai 
# str('chai')             #yai human friendly version hota hai string represent karta hai 
# print(str('chai'))
# print('chai')
# print(1<3)

# greater= (x<y) and (y<z)
# print(greater)

# import math
# print(math.floor(3.5))     #floor closet number below value deta g=hai jaise
# print(math.floor(-3.5))     #3.5 ka below 3 and -3.5 ka below -4 


# print(math.trunc(2.8))      #trunc zero ka pass lekar jata hai matlab 2.8 se 0 ka pass 2 hai isliya
# print(math.trunc(-2.8))     #idhar bhi -2 aaiga kyoki 0 ka pass -2 hai naki -4 


# print((2+1j)*2)

import random
print(random.random())
print(random.randint(1,10))

l1=['lemon','ginger','masala','mint']
print(random.choice(l1))

random.shuffle(l1)    #suffle function ko direct print nhi kara sakta kyoki suffle kuch return nhi karta isliya putput none aata hai 
print(l1)

add=0.1+0.1+0.4
add1=0.1+0.1+0.1-0.3
print(add)
print(add1)    #yai wrong way hai isko shi karna ka liya 

from decimal import Decimal    #isma D bada hi aaiga
print(Decimal('0.1') + Decimal('0.1')+ Decimal('0.1'))
print(Decimal('0.1') + Decimal('0.1')+ Decimal('0.1') - Decimal('0.3'))

setone={1,2,3,4}
print(setone)
settwo={1,3}
print(setone & settwo)     #intersection
print(setone|settwo)       #union
print(setone-setone)   #difference    #yaha empty set aisa denote hota hai Set() because {} to set hota hai 
print(type({}))