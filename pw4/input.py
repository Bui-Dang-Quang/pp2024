import math
from domain import person ,Student, Course

def studentList():
    students = []
    while True:
        try:
            no_Student = int(input("\nEnter the number of student: "))
            if no_Student < 1:
                print("Please provide at least 1 student: ")
            for i in range(no_Student):
                student_id = input("Student ID: ")
                student_name = input("Student's Name: ")
                dob = input("DoB: ")
                student = Student(student_id,student_name,dob)
                students.append(student)
            break
        except ValueError:
            print("Invalid Input, Please Try Again!")
    return students


def MarkInput(selected_course,students):
    marks = {}

    print(f"\nMark for student in {selected_course.getCourseName()} course: ")
    for student in students:
        while True:
            try: 
                mark = math.floor(float(input(f"Enter mark for {student.getStudentName()}: ")))
                marks[student.getStudentName()] = mark
                break
            except ValueError:
                print("Invalid Input, Please Try Again! ")
    return marks

def CreditInput(selected_course):
    while True:
        try:
            credits = int(input(f"Enter credits  for {selected_course.getCourseName()}: "))
            selected_course.setCredits(credits)
            break
        except ValueError:
            print("Invalid Input, Please Try Again! ")

def courseList(info):
    while True:
        try:
            info.no_Course = int(input("\nEnter the number of course: "))
            if info.no_Course < 1:
                print("Please provide at least 1 course: ")
            else:
                break
        except ValueError:
                print("Invalid! ")
    for i in range(info.no_Course):
        course_id = input("Course ID: ")
        course_name = input("Course's Name: ")
        course = Course(course_id,course_name)
        info.addCourse(course)
        CreditInput(course)

    return info


def selectedCourse(info):
    if info.no_Course == 0:
        print("Please input courses first!")
        return

    while True:
        selected_course_name = input("Select course by entering name: ")
        for course in info.courses:
            if course.getCourseName() == selected_course_name:
                print("\nSelected Course Information:")
                print(course)
                marks = MarkInput(course, info.students)
                info.marks[selected_course_name] = marks
                return
        print("Invalid Option. Please try again.")




