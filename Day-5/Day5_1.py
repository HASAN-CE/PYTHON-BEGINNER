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
Dict.update({"Name":"Js" , "Editor" : "Vs Code"})
print(Dict)
#here there is one key-value pair that is initially not present in dictionary so now it will add this key value pair in the dictionary

#5).get()
print(Dict.get(1991))

print(Dict.get("Name1")) #Prints None value
print(Dict["Name1"]) #Returns An Error 

#6).clear()
#7).copy()
#8).popitem()