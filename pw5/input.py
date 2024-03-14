import math
import os
import zipfile
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
    student_text_file = open("Student.txt","w")
    for student in students:
        student_text_file.write(student.__str__() + "\n")
    student_text_file.close()
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
    courses = []
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
        courses.append(course)
        CreditInput(course)
    course_text_file = open("Courses.text","w")
    for course in courses:
        course_text_file.write(course.__str__() + "\n")
    course_text_file.close()
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
                marks_text_file = open(f"{course.getCourseName()}_Marks.txt", "w")
                for student_name, mark in marks.items():
                    marks_text_file.write(f"Student: {student_name}, Mark: {mark}\n")
                return
        print("Invalid Option. Please try again.")

def compress_files():
    file_names = ["Student.txt", "Courses.text"]
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if name.endswith("_Marks.txt"):
                file_names.append(os.path.join(root, name))
    
    archive_name = "students.zip"
    zip_file = zipfile.ZipFile(archive_name, "w")
    for file_name in file_names:
        zip_file.write(file_name)

    print(f"All files have been compressed into {archive_name}")



