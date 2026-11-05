students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / n if n > 0 else 0

print("Average Marks:", average)