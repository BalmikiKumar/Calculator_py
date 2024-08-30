# x=int (input("Enter any number :"))
# count=0
# for i in range(1,x+1,1):
#     if(x%i==0):
#         count=count+1
# if(count==2):
#     print("Prime number")
# else:
#     print("Not prime number")

# SECOND METHOD OF PRINT PRIME NUMBER

# # n=int(input("Enter the number:-"))
# # if n>0:
# #     for i in range(2,n):
# #         if n%i==0:
# #             print(n, "Is not prime number")
# #             break
# #     else:
# #         print(n,"Is Prime Number")


# PRINT MARKSHEET OF STUDENTS AND ALL DETAILS LIKE AS NAME , ROLL , COURSE note in this code 2 method is include
class Student:
    # def S_details(self,a,b,c):
    #     self.name=a
    #     self.roll=b
    #     self.course=c
    def S_details(self):
        name=input("Enter student name")
        roll=int(input("Enter student roll no."))
        course=input("Enter student course")
        print("STUDENT NAME ==",name,"\nSTUDENT ROLL ==",roll,"\nSTUDENT COURSE==",course)
    def Marks(self,e,f,g):
        self.html=e
        self.css=f
        self.js=g
    def findTotal(self):
        tm=self.html+self.css+self.js
        return tm
    def Percentage(self):
        self.pm=(self.findTotal()/3)
    def PrintMarks(self):
        print("Total marks =",self.findTotal(),"\nPercentage =",self.pm)
        
obj=Student()
# m=(input("Enter name :"))
# n=int(input("Enter roll :"))
# o=(input("Enter course :"))
# obj.S_details(m,n,o)

obj.S_details()


A=int(input("Enter html marks :"))
B=int(input("Enter css marks :"))
C=int(input("Enter js marks :"))
obj.Marks(A,B,C)
# obj.findTotal()
obj.Percentage()
obj.PrintMarks()
