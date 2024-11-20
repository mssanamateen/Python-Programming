class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")


class Sports(Student):
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport

 
    def display_info(self):
        print(f"Sports Student: {self.name}, Age: {self.age}, Sport: {self.sport}")


class Skills(Student):
    def __init__(self, name, age, skills):
        super().__init__(name, age)
        self.skills = skills

  
    def display_info(self):
        print(f"Skills Student: {self.name}, Age: {self.age}, Skills: {', '.join(self.skills)}")


robinsports = Sports("Robin", 22, "Football")
robinskills = Skills("Robin", 22, ["Python", "ML", "DataScience"])



robinsports.display_info()    
robinskills.display_info()    
