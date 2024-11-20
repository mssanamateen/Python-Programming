class Student:
    def __init__(self,name,yr):
        self.name=name
        self.yr=yr

    def display_stud_details(self):
        print(f"Name:{self.name}, class:{self.yr}")


class Skills:
    def __init__(self,sk1,sk2,sk3):
        self.sk1=sk1
        self.sk2=sk2
        self.sk3=sk3
    def skills(self):
        print(f"Skills are {self.sk1},{self.sk2},{self.sk3}")

class BestStudent(Student,Skills):
    def __init__(self,fname,cls,sk1,sk2,sk3,rno):
        Student.__init__(self,fname,cls)
        Skills.__init__(self,sk1,sk2,sk3)
        self.rno=rno

    def display_student(self):
        print("The best Student...")
        self.display_stud_details()
        self.skills()
        print(f"student id:{self.rno}",end="\n")


robin=BestStudent("Robin Thomas Antony","4th year","Data Science","Machine Learning","Artificial Intelligence",27)
thejas=BestStudent("Thejas","4th year","Machine Learning","Artificial Intelligence","Deep Learning",124)
zafeer=BestStudent("Zafeer","4th year","Data Science","Machine Learning","Artificial Intelligence",10)
sainath=BestStudent("sainath","3rd year","python programming","AI","Kotlin",10)


robin.display_student()
thejas.display_student()
zafeer.display_student()
sainath.display_student()
