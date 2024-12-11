'''
For n=3

  *
 ***
*****

'''

n = int(input('Enter the number: '))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

#'end' paramete in print() function is used to specify what should be print at the end of the output