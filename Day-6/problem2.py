sub1 = int(input("Enter marks of 1 subject: "))
sub2 = int(input("Enter marks of 2 subject: "))
sub3 = int(input("Enter marks of 3 subject: "))

total = sub1 + sub2 + sub3 / 3
percentage = (total/300)*100
total_percentage = float(percentage)
print('Your percentage is: ',total_percentage)

if(percentage>40 and sub1>=33 and sub2>=33 and sub3>=33):
    print('Congratulations!! You Pass',total_percentage)
else:
    print('You Fail!! Better luck next year',total_percentage)
    