import math
from domain import Student,Course

def printStudentInformation(students):
    print("\nStudent's Information: ")
    for student in students:
        print(student.__str__())

def printCourseInformation(courses):
    print("\nCourse's Information: ")
    for course in courses:
        print(course.__str__())

def printMarkInformation(marks):
    print("\nScore in Selected Course: ")
    for course_name, course_marks in marks.items():
        print(f"\nCourse: {course_name}")
        for student_name,mark in course_marks.items():
            print("Student Name:",student_name,", Marks:",mark)

def GPA_CAL(info):
    student_gpa = {}

    for student in info.students:
        student_name = student.getStudentName()
        totalgrade = 0
        totalcredits = 0

        for course in info.courses:
            course_name = course.getCourseName()
            course_credits = course.getCredits()

            if course_name in info.marks and student_name in info.marks[course_name]:
                mark = info.marks[course_name][student_name]
                if isinstance(mark,int):
                    totalgrade = totalgrade + mark * course_credits
                    totalcredits = totalcredits + course_credits

        if totalcredits > 0:
            gpa = totalgrade / totalcredits
            student_gpa[student_name] = gpa
        else:
            student_gpa[student_name] = None
    
    sorted_gpa = sorted(student_gpa.items(),key=lambda x: x[1], reverse=True) #

    print("\nGPA for each student: ")
    for student_name,gpa in sorted_gpa:
        if gpa is not None:
            print(f"Student's Name: {student_name}, GPA: {gpa:.2f}")
        else:
            print(f"Student's Name: {student_name}, No GPA available (no credits)")

