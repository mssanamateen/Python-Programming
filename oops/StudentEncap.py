class StudentEncap:
    def __init__(self,stud_id,name,pwd,marks):
        #private members
        self.__stud_id=stud_id
        self.__pwd=pwd
        #protected members
        self._name=name
        self._marks=marks

    def get_student_id(self):
        return self.__stud_id

    def validate_pwd(self,pwd):
        return pwd==self.__pwd

    def display_marks(self):
        return self._marks

student=StudentEncap(10,"sainath","pass123",95)


print(student._name)


print(student.get_student_id())


print(student.validate_pwd('pass123'))

print(student.display_marks())
