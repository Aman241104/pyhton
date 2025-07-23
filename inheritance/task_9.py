# Problem Description: School Management System
# Objective:  
# Create a program that simulates a school management system with inheritance. There are four classes:  
# 1. Person (Base Class): Represents a general person with attributes like name and age
#    - Methods:
#      -__init__: Initializes the name and age.
#      - input_details: Takes input for name and age.
#      - display_details: Displays the name and age.
#      - greet: Prints a generic greeting message.
# 2. Student (Derived Class): Inherits from Person and adds attributes like grade and roll_number.  
#    - Methods:
#      - __init__: Initializes name, age, grade, and roll number.
#      - input_details: Takes input for grade and roll number in addition to name and age.
#      - display_details: Displays all student details.
#      - study: Prints a message indicating the student is studying.
# 3. Teacher (Derived Class): Inherits from Person and adds attributes like subject and salary
#    - Methods:
#      - __init__: Initializes name, age, subject, and salary.
#      - input_details: Takes input for subject and salary in addition to name and age.
#      - display_details: Displays all teacher details.
#      - teach: Prints a message indicating the teacher is teaching.
# 4. Administrator (Derived Class): Inherits from Person and adds attributes like department and role.  
#    - Methods:
#      - __init__: Initializes name, age, department, and role.
#      - input_details: Takes input for department and role in addition to name and age.
#      - display_details: Displays all administrator details.
#      - manage: Prints a message indicating the administrator is managing the school.


class person:
    def __init__(self):
        self.name=""
        self.age=0

    def person_details(self):
        self.name=input("Enter Your Name Here: ")
        self.age=int(input("Enter Your Age Here: "))

    def person_display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class student(person):
    def __init__(self):
        self.grade=""
        self.rnum=0

    def student_details(self):
        self.garde=input("Enter Your Grade: ")
        self.rnum=int(input("Enter Your roll number: "))

    def student_display(self):
        print("---------Studnet Details---------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Garde: {self.garde}")
        print(f"Roll number: {self.rnum}")

    def study(self):
        print(f"{self.name} is assigned {self.rnum} roll number.")

class teacher(person):


    def __init__(self):
        self.sub=""
        self.sal=0

    def teacher_details(self):
        self.sub=input("Enter Subject: ")
        self.sal=int(input("Enter Salary: "))

    def teacher_display(self):
        print("---------Teacher Details---------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.sub}")
        print(f"Salary: {self.sal}")

    def teach(self):
        print(f"{self.name} is assigned to teach {self.sub}.")

class administrator(person):
    def __init__(self):
        self.dep=""
        self.role=""

    def adm_details(self):
        self.dep=input("Enter Department: ")
        self.role=(input("Enter Role: "))

    def adm_display(self):
        print("---------Administrator Details---------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.dep}")
        print(f"Role: {self.role}")

    def adm(self):
        print(f"{self.name} is assigned to departmnet {self.dep}.")

f=True
while(flag == True):
    print("----------Menu----------")
    print("Enter 1 For Student Details.")
    print("Enter 2 For Teacher Details.")
    print("Enter 3 For Administrator Details.")
    print("Enter 4 to exit.")
    ch=int(input("Enter Your choice:"))

    if(ch == 1):
        s1=student()
        s1.person_details()
        s1.student_details()
        s1.student_display()
        s1.study()
    elif(ch == 2):
        t1=teacher()
        t1.person_details()
        t1.teacher_details()
        t1.teacher_display()
        t1.teach()
    elif(ch == 3):
        a1=administrator()
        a1.person_details()
        a1.adm_details()
        a1.adm_display()
        a1.adm()
    elif(ch == 4):
        flag=False
        exit