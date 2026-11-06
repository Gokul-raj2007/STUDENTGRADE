

name = input("Enter student name: ")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))
mark4 = int(input("Enter mark 4: "))
mark5 = int(input("Enter mark 5: "))


total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5


if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"


print("\n----- Student Grade Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")
