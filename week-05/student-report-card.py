#Dummy data
students_data = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

class Student:
    def __init__(self, name, marks):
        #Gets students name and list of marks
        self.name = name
        self.marks = marks

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return 'A'
        elif avg >= 65:
            return 'B'
        elif avg >= 50:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'

    def display(self):
        avg = self.average()
        status = "Pass" if avg >= 40 else "Fail"
        print(f"Name: {self.name}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {self.grade()}")
        print(f"Status: {status}")
        print("----------------------------")

print("=== STUDENT REPORT CARDS ===")

for name, marks in students_data:
    student = Student(name, marks)
    student.display()
