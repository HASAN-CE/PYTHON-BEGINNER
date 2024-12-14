def rem(list1,word="an"):
    n =[]
    for item in list1:
        if not(item==word):
            n.append(item.strip(word))
    return n
        
list1= ["Java","Python"]
print(rem(list1))