s = set()
s.add(20)
s.add(20.0)
s.add("20")

print("Length of the set is: ",len(s))
print(s)

#as a Python checks that the value of both the element are same it doenot than check the datatype

if (1 == '1'):
    print("True")
else:
    print("False")
    
#From this we can Interpret that for set in python 1 and 1.0 is same 