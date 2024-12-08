#String Functions

a = '''hASAN.S.RANGOONI'''
words = ["HASAN","RANGOONI"]
b = "I AM GOOD AT PROGRAMING AND BOTH HACKING"

print(len(a))
print(a.endswith("OONI"))
print(a.startswith("HASA"))
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