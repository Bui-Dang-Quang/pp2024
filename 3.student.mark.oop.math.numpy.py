import math
import numpy as np

class person():
    def __str__(self):
        pass

class Student(person):
    def __init__(self,sid,sname,dob):
        self.__studentID = sid
        self.__studentName = sname
        self.__DoB = dob

    def getStudentID(self):
        return self.__studentID
    
    def getStudentName(self):
        return self.__studentName
    
    def getDoB(self):
        return self.__DoB
    
    def __str__(self):
        return "Student ID: " + self.getStudentID() + ", Student's Name: " + self.getStudentName() + ", DoB: " + self.getDoB()
    

class Course(person):
    def __init__(self,cid,cname):
        self.__CourseId = cid
        self.__CourseName = cname
        self.__credits = 0
    
    def getCourseID(self):
        return self.__CourseId
    
    def getCourseName(self):
        return self.__CourseName
    
    def setCredits(self,credits):
        self.__credits = credits

    def getCredits(self):
        return self.__credits
    
    def __str__(self):
        return "Course ID: " + self.getCourseID() + ", Course's Name: " + self.getCourseName() + ", Credits: " + str(self.getCredits())

class StudentInformation:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.no_Course = 0
    
    def addStudent(self,student):
        return self.students.append(student)
    
    def addCourse(self,course):
        return self.courses.append(course)

    def studentList(self):
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
                    self.addStudent(student)
                break
            except ValueError:
                print("Invalid Input, Please Try Again!")

    def printStudentInformation(self):
        print("\nStudent's Information: ")
        for student in self.students:
            print(student.__str__())
    
    def MarkInput(self,selected_course):
        marks = {}

        print(f"\nMark for student in {selected_course.getCourseName()} course: ")
        for student in self.students:
            while True:
                try: 
                    mark = math.floor(float(input(f"Enter mark for {student.getStudentName()}: ")))
                    break
                except ValueError:
                    print("Invalid Input, Please Try Again! ")
            marks[student.getStudentName()] = mark
        self.marks[selected_course.getCourseName()] = marks

    def CreiditInput(self,selected_course):
        while True:
            try:
                credits = int(input(f"Enter credits  for {selected_course.getCourseName()}: "))
                selected_course.setCredits(credits)
                break
            except ValueError:
                print("Invalid Input, Please Try Again! ")

    def courseList(self):
        while True:
            try:
                self.no_Course = int(input("\nEnter the number of course: "))
                if self.no_Course < 1:
                    print("Please provide at least 1 course: ")
                else:
                    break
            except ValueError:
                print("Invalid! ")
        for i in range(self.no_Course):
            course_id = input("Course ID: ")
            course_name = input("Course's Name: ")
            course = Course(course_id,course_name)
            self.addCourse(course)
            self.CreiditInput(course)

    def printCourseInformation(self):
        print("\nCourse's Information: ")
        for course in self.courses:
            print(course.__str__())

    def selectedCourse(self):
        if self.no_Course == 0:
            print("Please input courses first! ")
            return

        while True:
            selectedcourse = input("Select course by entering name: ")
            for course in self.courses:
                if course.getCourseName() == selectedcourse:
                    print("\nSelected Course Information: ")
                    print(course.__str__())
                    self.MarkInput(course)
                    return False
            print("Invalid Option, please try again! ")
    
    def printMarkInformation(self):
        print("\nScore in Selected Course: ")
        for course_name, course_marks in self.marks.items():
            print(f"\nCourse: {course_name}")
            for student_name,mark in course_marks.items():
                print("Student Name:",student_name,", Marks:",mark)
    
    def GPA_CAL(self):
        student_gpa = {}

        for student in self.students:
            student_name = student.getStudentName()
            totalgrade = np.array(0)
            totalcredits = np.array(0)

            for course in self.courses:
                course_name = course.getCourseName()
                course_credits = course.getCredits()

                if course_name in self.marks and student_name in self.marks[course_name]:
                    mark = self.marks[course_name][student_name]
                    if isinstance(mark,int):
                        totalgrade = totalgrade + np.array(mark * course_credits)
                        totalcredits = totalcredits + np.array(course_credits)

            if totalcredits > 0:
                gpa = totalgrade / totalcredits
                student_gpa[student_name] = gpa.item()
            else:
                student_gpa[student_name] = None
        
        sorted_gpa = sorted(student_gpa.items(),key = lambda x: x[1], reverse=True) #

        print("\nGPA for each student: ")
        for student_name,gpa in sorted_gpa:
            if gpa is not None:
                print(f"Student's Name: {student_name}, GPA: {gpa:.2f}")
            else:
                print(f"Student's Name: {student_name}, No GPA available (no credits)")

            

    def displayMenu(self):
        while True:

            print("""\n
                      ==============================User option====================================
                      |         0. Exit program                                                   |
                      |         1. Input the Student's Information                                |
                      |         2. Input the Course's Information and credits                     |
                      |         3. Input Mark for students                                        |
                      |         4. List all the Course's Information                              |
                      |         5. List all the Student's Information                             |
                      |         6. List all Student's mark                                        |
                      |         7. List GPA(descending order)                                     |
                      =============================================================================
                """)
            
            try:
                choice = int(input("Choose the option: "))
                
                if choice == 0:
                    print("Exiting program... ")
                    break
                elif choice == 1:
                    self.studentList()
                elif choice == 2:
                    self.courseList()
                elif choice == 3:
                    self.selectedCourse()
                elif choice == 4:
                    self.printCourseInformation()
                elif choice == 5:
                    self.printStudentInformation()
                elif choice == 6:
                    self.printMarkInformation()
                elif choice == 7:
                    self.GPA_CAL()
                else:
                    print("Invalid choice. Please choose a number between 0 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            
info = StudentInformation()
info.displayMenu()