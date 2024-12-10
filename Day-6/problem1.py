a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

#Here the difference between 'or' & 'and'(Logical Operator) is that 'or' will execute the if-elif statement even the first condition match in statement & 'and' will only execute the if-elif statement  when all conditions match in if-elif statement


#Example with 'and' operator
if(a>b and a>c and a>d):
    print(f'{a} is Greatest')
elif(b>a and b>c and b>d):
    print(f'{b} is Greatest')
elif(c>a and c>b and c>d):
    print(f'{c} is Greatest')
elif(d>a and d>b and d>d):
    print(f'{d} is Greatest')


#Example with 'or' operator
if(a>b or a>c or a>d):
    print(f'{a} is Greatest')
elif(b>a or b>c or b>d):
    print(f'{b} is Greatest')
elif(c>a or c>b or c>d):
    print(f'{c} is Greatest')
elif(d>a or d>b or d>d):
    print(f'{d} is Greatest')
