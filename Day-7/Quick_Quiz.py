# print 'Python' 10 times using while loop

# a = 0
# while (a<10):
#     print('Python')
#     a+=1
    
# print('Exiting...')

#write the content of the list using while loop

list = [1,45,65,'Python','Js','Go','Shell',True,None,1235,65]

print('printing list with len method\n')
l = 0
while(l<len(list)):
    print(list[l])
    l+=1

print('\nPrinting without len method...')
#Without using len method
for i in list:
    print(i)
