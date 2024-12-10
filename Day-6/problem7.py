Post = input('Enter the post: ')

#1)Solution
if "Cyber" in Post:
    print('Post is taking about Cyber')
else: 
    print('Post is not  taking about Cyber')


#2)Solution
if "Cyber".upper() in Post.upper():
    print('Post is taking about Cyber')
else: 
    print('Post is not  taking about Cyber')