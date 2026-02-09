# python dictionary 

person= {
    "firstname" : "Jeffery" ,
    "lastname"  :  "Epstein" ,
    "Age" : 73 ,
    "colors" : ["white" , "black" ] ,
    "salary" : 300
}

# show output
print(person)

# print age
print(person["Age"])

# print salary
print(person["salary"])

# add new key value 
person["passport"] = "B008Hn"

# show output
print(person)

# change age to 34 
person["Age"] = 34

# show output
print(person) 

# delete lastname
del person["lastname"]

# show output
print(person)


