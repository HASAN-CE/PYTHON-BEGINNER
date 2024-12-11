#Default Arguments
# Since the end argument is not changing and remains the same, we can set it as a default argument
def Greet(name,end):
    print(f'Dear, {name} {end}')
    
Greet('John','Thank you for Coming')
Greet('Payal','Thank you for Coming')
Greet('Harry','Thank you for Coming')


#Default Arguments Example
def Greet1(name,end='Thanks for coming'):
    print(f'Dear, {name} {end}')
    
print('\nWith the default arguments')
Greet1('John')
Greet1('Payal')
Greet1('Harry')