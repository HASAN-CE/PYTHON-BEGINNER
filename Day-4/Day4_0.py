#Lists 
#As Lists are Mutable so here we are able to change the 0th index element 
list1 = ["Helper","Program","Cyber",56,False,None,468.5,"This"]
print(list1)

#here it will change the existing list but not create the new list
print(list1[0])
list1[0]="Hacker"
print(list1)  
