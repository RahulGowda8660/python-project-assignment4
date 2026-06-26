import re

student = {
    "Alice": 89,
    "Priya": 79
}

student_name = input("Enter your name: ")

pattern = r"Alice|Priya"

match_object = re.search(pattern, student_name)

if match_object:
    print(f"Match is found in {student_name}")
    print(f"Marks: {student[student_name]}")
else:
    print(f"Match is not found in {student_name}")