n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

print('The Greatest of all 3 number is: ',(greatest(n1,n2,n3)))