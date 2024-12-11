#Sumation of the n numbers
n = int(input('Enter the number: '))
i = 0
sum = 0 
while(i<=n):
    sum = sum + i
    i = i+1  

print(f"Sum of {n} is",sum)

#Multiplication of the n numbers
i = 1
mul = 1 
while(i<=n):
    mul = mul * i
    i = i+1  

print(f"Multiplication of {n} is",mul)
