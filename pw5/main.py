from input import studentList, courseList, selectedCourse,compress_files
from output import printStudentInformation, printCourseInformation, printMarkInformation, GPA_CAL
from domain import Student, Course

class StudentInformation:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.no_Course = 0
    
    def addStudent(self, student):
        self.students.append(student)
    
    def addCourse(self, course):
        self.courses.append(course)

def main():  
    info = StudentInformation()
    while True:
        print("""\n
            ==============================User option====================================
            |         0. Exit program                                                   |
            |         1. Input the Student's Information                                |
            |         2. Input the Course's Information                                 |
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
                compress_files()
                print("Exiting program... ")
                break
            elif choice == 1:
                info.students = studentList()
            elif choice == 2:
                courseList(info)
            elif choice == 3:
                selectedCourse(info)
            elif choice == 4:
                printCourseInformation(info.courses)
            elif choice == 5:
                printStudentInformation(info.students)
            elif choice == 6:
                printMarkInformation(info.marks)
            elif choice == 7:
                GPA_CAL(info)
            else:
                print("Invalid choice. Please choose a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
