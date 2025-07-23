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

        with open('reportcard.txt','w') as report:
            report.write(f"Name: {self.name}\n")
            report.write(f"Roll Number: {self.rollno}\n")
            report.write(f"Class: {self.cla}\n")
            report.write("----------Marks----------\n")
            report.write(f"Maths: {self.maths}\n")
            report.write(f"English: {self.eng}\n")
            report.write(f"Hindi: {self.hindi}\n")
            report.write(f"Gujrati: {self.guj}\n")
            report.write(f"Science: {self.sci}\n")
            report.close()



    def grade(self):
        self.total=(self.maths+self.eng+self.sci+self.hindi+self.guj)
        self.per=((self.total * 100)/500)

        with open('reportcard.txt','a') as report:
            report.write("-------------------------\n")
            report.write(f"Total: {self.total}\n")
            report.write(f"Percentage: {self.per} % \n")
            report.close()

        match self.per:
            case _ if 90<self.per:
                self.grade="A"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"Nerd!!\n")
                    report.close()
                
            case _ if (80<self.per) and (self.per>=90):
                self.grade="B"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"Nice Job kid!!\n")
                    report.close()

            case _ if 70<self.per and self.per>=80:
                self.grade="C"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"Good Enough!!\n")
                    report.close()

            case _ if 60<self.per and self.per>=70:
                self.grade="D"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"LOL!!\n")
                    report.close()

            case _ if 50<self.per and self.per>=60:
                self.grade="E"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"Stupid!!\n")
                    report.close()

            case _ if self.per<=50:
                self.grade="F"
                with open('reportcard.txt','a') as report:
                    report.write("-------------------------\n")
                    report.write(f"Grade: {self.grade}\n")
                    report.write(f"Better luck next time!!\n")
                    report.close()

            case _:
                print("Not Valid\n")
        

    def display(self):  
        with open('reportcard.txt', "r") as file:
                print(file.read())

stu1 = report()
stu1.grade()
stu1.display()