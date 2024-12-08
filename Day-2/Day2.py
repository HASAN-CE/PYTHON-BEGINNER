#Topic-Variables And DataTypes

#variables are like a container to store the values

#Example

a = 10       #a is an integer
b = 25.2     #b is an float
c = "HASAN"  #c is an String 
d = True     #d is an boolean
e = None     #e is an none
#type() function is used to check the datatype of a variable
ax = type(a)
bx = type(b)
cx = type(c)
dx = type(d)
ex = type(e)

#print all Information
print(a,"is",ax)
print(b,"is",bx)
print(c,"is",cx)
print(d,"is",dx)
print(e,"is",ex)



#here a,b,c,,e are like identifiers 
#in a variable name there cannot be WhiteSpace


#operators:-
#Arithmetic operators: +,-,/,*, etc. 
#Assignment operators: =,+=,-=, etc.  
#Comparison operators: ==,>,<,>=,<=,!=, etc.   (NORMALLY IT RETURNS THE BOOLEAN VALUE)
#Logical operators: and,or,not,  etc.

#example of arithmetic operators
a = 15
b = 20
c = a+b
print(c)
#example of coparison operators
d = 9
print(d)
d+=d
print(d)
#example of logical operators
print(not(True))  #basically 'not' returns the opposite value of that operand 