#Dictionary Methods

Dict = {
    "Name" : "Python",
    "Age" : 33,
    "Owner" : "Guido van Rossum",
    "Libraries" : ["NumPy","SciPy","TensorFlow"],
    1991 :  "Birth_year",
}

# print(Dict)

#Methods
 
#1).items()
print(Dict.items())

#2).keys()
print(Dict.keys())

#3).values()
print(Dict.values())

#4).update().
Dict.update({"Name":"Js"})
print(Dict)