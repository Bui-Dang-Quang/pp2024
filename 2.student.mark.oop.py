class Person:
    def __str__(self):
        pass

class Student(Person):
    # Setter
    def setstudentid(self,stuid):
        self.__student_id = stuid
    def setstudentname(self,stuna):
        self.__student_name = stuna
    def setDoB(self,dob):
        self.__DoB = dob
    
    # Getter
    def getstudentid(self):
        return self.__student_id
    def getstudentname(self):
        return self.__student_name
    def getDoB(self):
        return self.__DoB
    
    # same as toString() function - Java
    def __str__(self):
        return "Student ID: " + self.getstudentid() + ", Student's Name: " + self.getstudentname() + ", DoB: " + self.getDoB()
    

class Course(Person):
    # Setter
    def setcourseid(self,couid):
        self.__course_id = couid
    def setcoursename(self,couname):
        self.__course_name = couname
    
    # getter 
    def getcourseid(self):
        return self.__course_id
    def getcoursename(self):
        return self.__course_name
    
    def __str__(self):
        return "Course ID: " + self.getcourseid() + ", Course's Name: " + self.getcoursename()
    

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
    
    def addstudent(self, student):
        return self.students.append(student)
    def addcourse(self, course):
        return self.courses.append(course)
    
    def inputmark(self):
        marks = {}
        print("\nEnter marks for students: ")
        for student in self.students:
            mark = input(f"Enter mark for {student.getstudentname()}:")
            marks[student.getstudentname()] = mark
        return marks
    
    def liststudentinfo(self):
        no_Student = int(input("Enter the number of student: "))
        for i in range(no_Student):
            student_id = input("Student ID: ")
            student_name = input("Student Name: ")
            DoB = input("DoB: ")
            student = Student()
            student.setstudentid(student_id)
            student.setstudentname(student_name)
            student.setDoB(DoB)
            self.addstudent(student)
        
        print("\nStudent's Infromation:")
        for student in self.students:
            print(student.__str__())

    def listcourseinfo(self,no_course):
        for i in range(no_course):
            course_id = input("Course ID: ")
            course_name =  input("Course's Name: ")
            course = Course()
            course.setcourseid(course_id)
            course.setcoursename(course_name)
            self.addcourse(course)    

        print("\nCourse's Information: ")
        for course in self.courses:
            print(course.__str__())
    
    def selectedcourse(self):
        no_course = int(input("Enter the number of course: "))
        self.listcourseinfo(no_course)
        selected_course = input("Select course by entering ID: ")
        for course in self.courses:
            if course.getcourseid() == selected_course:
                print("\nSelected Course Information:")
                print(course.__str__())
                mark_dictionary = self.inputmark()
                for student_name,mark in mark_dictionary.items():
                    print("Student Name",student_name,"Marks:",mark)
                break
            else:
                print("Invalid")

def main():
    sm = StudentManagement()
    sm.liststudentinfo()
    sm.selectedcourse()

if __name__ == "__main__":
    main()