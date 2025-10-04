# chai_types={"masala":"spicy","ginger":"Zesty","green":"mild"}
# # print(chai_types)
# # print(chai_types["masala"])
# # print(chai_types.get("ginger"))

# # print(chai_types.get("gingery"))    #or hum function ka sath work karta hai to error nhi aata none aata hai 
# # print(chai_types["masalaa"])     #idhar error aa rha hai kyoki ya simple method hai 
# #agar kissi bhi key a liya valuechange karna ho to yai karenga 
# # chai_types["green"]="fresh"
# # print(chai_types)
# # for chai in chai_types:
# #         print(chai,chai_types[chai])    #1st method to access key and value

# for key,value in chai_types.items():    #2nd method to access both key and value
#          print(key,value)

# if "masala" in chai_types:               #for checking
#         print("I have masala chai")

# #find length
# chai_typess={"masala":"tasty","ginger":"tadakadar"}
# print(chai_typess)
# print(len(chai_typess))
# chai_typess["lemon"]="mild"
# print(chai_typess)
# chai_typess.pop("ginger")   #koi specific karna hai to uski key deni hogi 
# print(chai_typess)
# chai_typess.popitem()      #agr huma dict mai se last item pop karna hai to popitem likhna hoga 
# print(chai_typess)

# # del chai_typess["masala"]
# # print(chai_typess)


# chai_types_copy=chai_typess.copy()
# print(chai_types_copy)

# tea_soap={
#     "chai":{"masala":"spicy","ginger":"zesty"},
#     "tea":{"green":"mild","black":"strong"}
# }
# print(tea_soap)
# print(tea_soap["chai"])
# print(tea_soap["chai"]["ginger"])


# squared_num = {x:x**2 for x in range(6)}       #x ka liya hum yaha range de diya jismai 6 include nhi hoga 
# print(squared_num)
# squared_num.clear()
# print(squared_num)

# keys=["masala","ginger","lemon"]
# print(keys)

# default_value="delicious"
# new_dict=dict.fromkeys(keys,default_value)
# print(new_dict)

# new_dict=dict.fromkeys(keys,keys)
# print(new_dict)

#tuples starts here---------   
#tuple is immutable-----

tea_types=("black","green","oolong")  #or yai hi chiz tupl hai to yai immutable hai no changable hai 
# # print(tea_types)
# print(tea_types[0])
# tea_types[0]="lemon"      # idhar error aaiga because yai change nhi ho sakta 
# print(tea_types)
# tea_typees=["black","green"]   #yai list hai isliya yai mutable/changable hai 
# tea_typees[0]="lemon"
# print(tea_typees)


# print(len(tea_types))
# more_tea=("herbal","earl grey")
# all_tea=more_tea + tea_types
# print(all_tea)
# if "green" in all_tea:
#         print("i have green tea")

more_tea=("herbal","earl grey","herbal")
print(more_tea)
print(more_tea.count("herbal"))

