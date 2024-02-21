
def No_Student():
    return int(input("Enter the number of student: "))

def student_info():
    student_id = input("ID Student: ")
    student_name = input("Student's Name: ")
    DoB = input("DoB: ")
    return {"Student's ID":student_id,"Student's Name":student_name,"DoB":DoB}

def No_Course():
    return int(input("\nEnter the number of course: "))

def Course_info():
    course_id = input("ID course: ")
    course_name = input("Course name: ")
    return {"Course's ID":course_id,"Course's Name":course_name}

def inputmark(students):
    marks = {}
    print("Enter marks for students:")
    for student in students:
        students_name = student["Student's Name"]
        students_id = student["Student's ID"]
        mark = float(input("Enter marks for " + students_name + " (Student ID:" + students_id + "): "))
        marks[students_name] = mark
    return marks

def list_student_info():
    no_student = No_Student()
    students = []
    for i in range(no_student):
        student = student_info()
        students.append(student)
    print("\nStudent's Information: ")
    for student in students:
        print(student)
    return students

# display courses and input mark for each student
def list_course_info(students):
    no_course = No_Course()
    courses = []

    for i in range(no_course):
        course = Course_info()
        courses.append(course)
        
    print("\nCourse's Infomation")
    for course in courses:
        print(course)
    
    selected_course_id = input("Select course by entering ID: ")

    ## find the selected course and print its information
    for course in courses:
        if course["Course's ID"] == selected_course_id:
            print("\nSelected Course Information: ")
            print(course)
        
        	## input marks for students in selected course
            mark_dictionary = inputmark(students)
            print("\nStudent's Mark:")
            for students_name,mark in mark_dictionary.items():
                print("Student Name",students_name,"Marks:",mark)
            break
        else:
            print("Invalid Course ID")

def main():
    students = list_student_info()
    list_course_info(students)

if __name__ == "__main__":
    main()
