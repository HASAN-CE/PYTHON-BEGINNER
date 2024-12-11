#Arguments in Function

#Single argument
def goodDay(name):
    print(f'Good Day,{name}')

goodDay('John')
goodDay('Payal')
goodDay('Harry')
goodDay('Rohan')


#Double argument
def Greet(name,end):
    print(f'Dear, {name} {end}')
    
Greet('John','Thank you for Coming')
Greet('Payal','Thank you for Coming')
Greet('Harry','Thank you for Coming')


#return keyword
def avg(a,b):
    return (a+b)/2

a = avg(7,2)
print("Average:",a)