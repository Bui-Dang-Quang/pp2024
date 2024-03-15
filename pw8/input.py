import math
import pickle
import threading
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
    def writestudentinfo():
        student_binary_file = open("Student.pkl","wb")
        pickle.dump(students,student_binary_file)
    Thread1 = threading.Thread(target=writestudentinfo)
    Thread1.start()
    Thread1.join()
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
            credits = int(input(f"Enter credits for {selected_course.getCourseName()}: "))
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
    def writecourseinfo():
        course_binary_file = open("Courses.pkl","wb")
        pickle.dump(courses,course_binary_file)
    Thread1 = threading.Thread(target=writecourseinfo)
    Thread1.start()
    Thread1.join()
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
                def writemarkinfo():
                    marks_binary_file = open(f"{course.getCourseName()}_Marks.pickle", "wb")
                    pickle.dump(marks,marks_binary_file)
                Thread1 = threading.Thread(target=writemarkinfo)
                Thread1.start()
                Thread1.join()
                return
        print("Invalid Option. Please try again.")


def load_data(file_name):
    try:
        file = open(file_name,"rb")
        data = pickle.load(file)
        return data
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return None
    except Exception as e:
        print(f"Error loading data from {file_name}: {e}")
        return None


def load_students_pkl():
    student_data = load_data("Student.pkl")
    if student_data is not None:
        for student in student_data:
            print(student)
    else:
        print("There's nothing inside! ")


def load_courses_pkl():
    course_data = load_data("Courses.pkl")
    if course_data is not None:
        for course in course_data:
            print(course)
    else:
        print("There's nothing inside! ")

