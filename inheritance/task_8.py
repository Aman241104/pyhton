#  Design a system where a person can be both a Student and a Faculty member. A person may have both student and faculty-specific actions.

class person:
    pass

class student(person):
    def stu(self):
        print("Student is *Doing Student stuffs*")

class faculty(person):
    def fact(self):
        print("faculty is *Doing faculty stuff stuffs*")
        

p1=person()
p1.stu()
p1.faculty()
