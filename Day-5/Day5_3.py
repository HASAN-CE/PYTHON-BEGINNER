#Set Methods
s = set() 
s = {"Python","Js",None,False,156,15,"html"}
print(s,type(s))

#1.add()
s.add(566)
print(s,type(s))

#2.remove()
s.remove(None)
print(s,type(s))
s.remove("Css")
print(s,type(s))  #Raises an error  

#3.copy()
s.copy()
print(s,type(s))

#4.clear()
s.clear()
print(s,type(s))