#String Functions

a = '''pYTHON PROGRAM'''
words = ["PYTHON","PROGRAMMING"]
b = "I AM GOOD AT PROGRAMING AND BOTH HACKING"

print(len(a))
print(a.endswith("MING"))
print(a.startswith("PYTHO"))
print(a.count("A"))
print(a.title())    
print(a.capitalize())
print(a.isalpha())
print(a.isdigit())
print(a.find("H"))
print(" ".join(words))
print(a.split("."))
print(a.strip())
print(a.lower())
print(a.upper())
print(b.replace("GOOD","EXCELLENT"))  # it take all occurences in the string