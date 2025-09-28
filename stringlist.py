# chai="lemon chai"
# print(chai)
# chai="masala chai"
# print(chai)
# first_char = chai[0]
# print(first_char)
# slice = chai[0:6]
# print(slice)
# chai2="ginger tea"
# slice_neg =chai2[-3:]
# print(slice_neg)
# reversed_all=chai[::-1]

# num_list ="0123456789"
# print(num_list[:])
# print(num_list[3:])
# print(num_list[:7])
# print(num_list[0:7:2])    #idhar third vala ka matlab hai 2-2 la gap

# chai="masala chai"
# print(chai)
# print(chai.lower())
# print(chai.upper())
# chai = "Masala chai"
# print(chai.strip())      #strip matlab spaces hata deta hai 
# print(chai.replace("Masala","Lemon"))
# chai = "Lemon,Ginger,Masala,Mint"
# print(chai.split())
# print(chai.split(","))


# chai="masala Chai" 
# print(chai.find("Chai"))
# chai="masala chai chai chai"
# print(chai.count("chai"))
# chai_type="masala"
# quantity=2
# order="i ordered {} cups of {} chai"
# print(order)
# print(order.format(quantity,chai_type))        #idher curly brace lagana sai hum variable put kar sakta hai 

# chai_variety=['lemon','masala','ginger']
# print(chai_variety)
# print(" ".join(chai_variety))

# chai="masala chai"
# print(len(chai))
# for letter in chai:
#     print(letter)



#List Starts here -------------------

# tea_varieties=['black tea','green tea',"oolong",'white']
# print(tea_varieties)
# print(tea_varieties[1])
# print(tea_varieties[-1])
# print(tea_varieties[1:3])
# print(tea_varieties[:2])
# tea_varieties[3]="herbal"
# print(tea_varieties)

tea_varieties=['black tea','green tea',"oolong",'white']
# print(tea_varieties[1:2])
# print(tea_varieties[1:2])=["lemon"]
# print(tea_varieties[1:3])=["green","masala"]   yai do line shamj nhi aai isse check karna hai 
# print(tea_varieties[1:1])

# print(tea_varieties)
# tea_varieties.pop()
# print(tea_varieties)
# tea_varieties.insert(1, "masala")
# print(tea_varieties)
tea_varieties_copy=tea_varieties.copy()
print(tea_varieties_copy)
tea_varieties_copy.append("lemon")
print(tea_varieties_copy)
print(tea_varieties)



