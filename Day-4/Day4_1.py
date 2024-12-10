#List Methods

l1  =  [1,1651,1668,1326,18641,511,316,615,9898,]
friends = ["Apple","Orange",5,345.06,False,None,"Karan"]
print(friends[1:5])

#1.append
friends.append("Sharma")
print(friends)

#2.sort
l1.sort()
print(l1)

#3.reverse
l1.reverse()
print(l1)

#4.insert 
friends.insert(5,"Arman")   # 5 is index for "Arman"
print(friends)

#5.pop 
friends.pop(1)
print(friends)

#6.remove 
l2=[1,2,56,165,4916,16,98,64,918]
l2.remove(56)  
print(l2)

#7.index() method return at which index the element is present
value = l2.index(98)
print(value)

