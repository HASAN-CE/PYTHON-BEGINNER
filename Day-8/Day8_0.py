#Functions 
#Here if we have to do the below task again and again the code snippet repetation make code more complex and longer to avoid this situation function comes at rescue 

# n1 = int(input('Enter First Number: '))
# n2 = int(input('Enter Second Number: '))
# n3 = int(input('Enter Third Number: '))

# total = n1+n2+n3
# print(total)

#to declare function use 'def' keyword

#Function definition
def add_number():
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    n3 = int(input('Enter Third Number: '))

    total = n1+n2+n3
    print("Total of the above number: ",total)

#Function call
add_number()