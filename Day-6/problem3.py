str1 = 'Make a lot of money'
str2 = 'Buy now'
str3 = 'Subscribe this'
str4 = 'Click this'

#1) First Solution
comment = input('Comment: ')
if(str1==comment):
    print('Spammer')
elif(str2==comment):
    print('Spammer')
elif(str3==comment):
    print('Spammer')
elif(str4==comment):
    print('Spammer')
else:
    print('Thanks for Commenting')



#2) Second Solution
# 'in' keyword is used to check the membership 
if((comment in str1)or(comment in str2)or(comment in str3)or(comment in str4)):
    print('Spammer')
else:
    print('Thanks for Commenting')