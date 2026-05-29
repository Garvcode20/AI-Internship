import json
import os

"""
TASK 1: Student Result Management System

AI Prompt Used (Simulated):
Initial Prompt: "Write a Python program for a student result management system."
Improved Prompt: "Write an interactive Student Result Management System in Python using classes. 
It should store marks, calculate percentages and grades, display topper details, and allow 
searching by roll number. Add comments and error handling."

Why the improved prompt produced better code:
The initial prompt resulted in a simple procedural script with no structure or error handling.
The improved prompt specified the use of classes (OOP), which made the code modular and easier to maintain. 
It also explicitly requested the necessary features, error handling, and comments, resulting in a production-ready template.

Manual Improvements & Additional Features Added:
1. Improved error handling for input validation (ensuring marks are between 0-100).
2. Added Feature 1: Data Persistence (saving and loading student records to/from a JSON file).
3. Added Feature 2: Class Statistics (calculating class average and pass percentage).
"""

DATA_FILE = "student_data.json"

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks  # Dictionary of subject: mark
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()

    def calculate_percentage(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 50:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "marks": self.marks,
            "percentage": self.percentage,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["roll_number"], data["name"], data["marks"])

    def display(self):
        print(f"\nRoll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")


class ResultManagementSystem:
    def __init__(self):
        self.students = {}
        self.load_data()

    def add_student(self):
        roll_number = input("Enter Roll Number: ")
        if roll_number in self.students:
            print("Student with this roll number already exists.")
            return

        name = input("Enter Student Name: ")
        marks = {}
        subjects = ["Math", "Science", "English"]
        
        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= mark <= 100:
                        marks[subject] = mark
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        new_student = Student(roll_number, name, marks)
        self.students[roll_number] = new_student
        self.save_data()
        print(f"Student {name} added successfully!")

    def search_student(self):
        roll_number = input("Enter Roll Number to search: ")
        student = self.students.get(roll_number)
        if student:
            student.display()
        else:
            print("Student not found.")

    def display_topper(self):
        if not self.students:
            print("No student records available.")
            return
        
        topper = max(self.students.values(), key=lambda s: s.percentage)
        print("\n--- Topper Details ---")
        topper.display()

    # Feature 2: Class Statistics
    def display_statistics(self):
        if not self.students:
            print("No student records available.")
            return
        
        total_students = len(self.students)
        total_percentage = sum(s.percentage for s in self.students.values())
        class_average = total_percentage / total_students
        
        passed_students = sum(1 for s in self.students.values() if s.grade != 'F')
        pass_percentage = (passed_students / total_students) * 100
        
        print("\n--- Class Statistics ---")
        print(f"Total Students: {total_students}")
        print(f"Class Average Percentage: {class_average:.2f}%")
        print(f"Pass Percentage: {pass_percentage:.2f}%")

    # Feature 1: Data Persistence
    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump({roll: student.to_dict() for roll, student in self.students.items()}, f, indent=4)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
                    self.students = {roll: Student.from_dict(s_data) for roll, s_data in data.items()}
            except json.JSONDecodeError:
                print("Error reading data file. Starting fresh.")
                self.students = {}

    def menu(self):
        while True:
            print("\n=== Student Result Management System ===")
            print("1. Add Student")
            print("2. Search Student")
            print("3. Display Topper")
            print("4. Class Statistics")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.search_student()
            elif choice == '3':
                self.display_topper()
            elif choice == '4':
                self.display_statistics()
            elif choice == '5':
                print("Exiting system. Data is saved automatically.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = ResultManagementSystem()
    system.menu()
