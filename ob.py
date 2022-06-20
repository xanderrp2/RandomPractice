##import pygame
##import random
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((1000,1000))
##pygame.display.set_caption("game1")
##
##
##
##
##
##class Shapes():
##    def __init__(self):
##        self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##        self.x = random.randint(0,1000)
##        self.y = random.randint(0,1000)
##class RECT(Shapes):
##    def __init__(self):
##        super().__init__()
##
##    def draw(self):
##        pygame.draw.rect(screen,self.colour,(self.x,self.y,10,20))
##        print("draw1")
##
##class CIRCLE(Shapes):
##    def __init__(self):
##        super().__init__()
##    def draw(self):
##        pygame.draw.circle(screen,self.colour,(self.x,self.y),50)
##        print("draw2")
##
##
##while True:
##    
##
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        if event.type == KEYDOWN:
##            if event.key == K_r:
##                A = RECT()
##                A.draw()
##
##            if event.key == K_k:
##                B = CIRCLE()
##                B.draw()
##
##            if event.key == K_s:
##                pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,1000),random.randint(0,100),15,15))
##                
##
##    pygame.display.update()
        
class Person():
    def __init__(self,first,last,email,DOB):
        self.first = first
        self.last = last
        self.email = email
        self.DOB = DOB

class Student(Person):
    def __init__(self,first,last,email,DOB,ID,GPA):
        super().__init__(first,last,email,DOB)
        self.ID = ID
        self.GPA = GPA
class Teacher(Person):
    def __init__(self,first,last,email,DOB,TeacherID,StudentList,ClassSize):
        super().__init__(first,last,email,DOB)
        self.TeacherID = TeacherID
        self.StudentList = StudentList
        self.ClassSize = ClassSize
    def show_student_info(self,student):
            print(student.email)
            print(student.first)
            print(student.GPA)
    def add_students(self,a):
        self.StudentList.append(a)
        print(self.StudentList)

    def remove_student(self,a):
        self.StudentList.pop(a)
        print(self.StudentList)
        
        
        
        
        

        
A = Student("A","1","A","AK","A1",4.9)
B = Student("B","2","B","BK","B2",4.9)
C = Student("C","3","C","CK","C3",2.3)
M = [A,B,C]



AA = Teacher("AA","AA1","AA@",1,17,[A,B,C],3)

AA.remove_student(1)

for i in AA.StudentList:
    AA.show_student_info(i)
print(issubclass(Student,Teacher))
    
