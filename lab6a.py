#!/usr/bin/env python3
# Author ID: isingh176

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert number to a string to avoid TypeError
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if len(self.courses) == 0:
            gpa = 0.0  # Handle ZeroDivisionError if no courses(solved for second problem)
        else:
            total_grades = sum(self.courses.values())
            gpa = total_grades / len(self.courses) if total_grades > 0 else 0.0
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Return a list of course that the student passed (grade > 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0] #final solution
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Student number as an integer(solved for first problem)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
