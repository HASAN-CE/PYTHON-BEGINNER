user_name = input('Enter the username: ')
print(user_name)

if(len(user_name)>10):
    print('Valid username')
elif(user_name<10):
    print('Invalid username')