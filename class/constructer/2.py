class report:
    def __init__(self):
        self.name = input("Enter Studnet Name:")  
        self.rollno = int(input("Enter roll number:"))
        self.cla=input("Enter Class:")
        self.maths=int(input("Enter marks for maths:"))
        self.eng=int(input("Enter marks for english:"))
        self.hindi=int(input("Enter marks for hindi:"))
        self.guj=int(input("Enter marks for gujarati:"))
        self.sci=int(input("Enter marks for science:"))


    def grade(self):
        self.total=(self.maths+self.eng+self.sci+self.hindi+self.guj)
        self.per=((self.total * 100)/500)

        match self.per:
            case _ if 90<self.per:
                self.grade="A"
            case _ if 80<self.per>=90:
                self.grade="B"
            case _ if 70<self.per>=80:
                self.grade="C"
            case _ if 60<self.per>=70:
                self.grade="D"
            case _ if 60<self.per>=40:
                self.grade="E"
            case _ if self.per<=40:
                self.grade="F"
            case _:
                print("Not Valid")
        

    def display(self):  
        print(f"name: {self.name}")
        print(f"roll number: {self.rollno}")
        print(f"name: {self.name}")
        print(f"Class: {self.cla}")
        print("----------Marks----------")
        print(f"Maths: {self.maths}")
        print(f"English: {self.eng}")
        print(f"Hindi: {self.hindi}")
        print(f"Gujarati: {self.guj}")
        print(f"Science: {self.sci}")
        print(f"Total:{self.total}/500")
        print(f"Percentage:{self.per}")
        print(f"Grade:{self.grade}")

stu1 = report()
stu1.grade()
stu1.display()