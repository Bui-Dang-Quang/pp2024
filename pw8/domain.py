import math

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
