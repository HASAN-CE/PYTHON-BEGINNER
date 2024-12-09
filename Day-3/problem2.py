# #Solution 1:-
# a = input("ENTER YOUR NAME: ")
# b = input("ENTER THE DATE: ")
# letter = (f" Dear,\n {a} You are selected\n On {b}")
# print(letter)

#Solution 2:-
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","ROHAN").replace("<|Date|>","12-5-25"))
#here we have done chainig of 'string.replace'
