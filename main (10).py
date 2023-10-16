class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def cgpa_key(student):
    return student.cgpa

students_list = [
    Student("John", "2021001", 3.9),
    Student("Jane", "2021002", 3.7),
    Student("Alice", "2021003", 3.8),
    Student("Bob", "2021004", 3.6)
]

sort_students = sorted(students_list, key=cgpa_key, reverse=True)

for student in sort_students:
    print(f"Name: {student.name},  Roll Number: {student.roll_number}, CGPA: {student.cgpa}")