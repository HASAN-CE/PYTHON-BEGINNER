# Creating a list to store student marks
marks = []

# Prompting the user to input marks for each student
M1 = int(input("ENTER MARKS FOR 1 STUDENT: "))
marks.append(M1)

M2 = int(input("ENTER MARKS FOR 2 STUDENT: "))
marks.append(M2)

M3 = int(input("ENTER MARKS FOR 3 STUDENT: "))
marks.append(M3)

M4 = int(input("ENTER MARKS FOR 4 STUDENT: "))
marks.append(M4)

M5 = int(input("ENTER MARKS FOR 5 STUDENT: "))
marks.append(M5)

M6 = int(input("ENTER MARKS FOR 6 STUDENT: "))
marks.append(M6)

# Sort the list of marks in ascending order
marks.sort()
print(marks)
