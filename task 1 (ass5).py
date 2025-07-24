# task1_student_marks.py

# Create a dictionary of students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

# Ask the user to enter a student's name
name = input("Enter the student's name: ")

# Check if the student exists in the dictionary
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
