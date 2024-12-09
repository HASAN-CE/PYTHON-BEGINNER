#Tuples Methods

a = (38,"MANAV",18,True,None,58,98,56,85,58,25,35,58,"SHAH")
print(a)

#count() method 
No = a.count(58)
print(No)
print(a)

#index() method
In = a.index(58)
print(In) 

#len() method
print(len(a))

#concatiton of a list of tuples
#As Tuple are immutable it creates whole new tuple doenot change the existing tuple
tup_1 = ("PYTHON","JS","RUBY","SHELL","RUST")
tup_2 = (1,2,3,4)
res = tup_1 + tup_2
print(res) 

#Different Tuple Methods
#min()
#max()
#sum()
#any()