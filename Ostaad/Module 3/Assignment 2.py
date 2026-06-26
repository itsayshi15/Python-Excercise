class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):
    def introduce(self):
        print("I am a student.")


class GraduateStudent(Student):
    def introduce(self):
        print("I am a graduate student.")


class Teacher(Person):
    def introduce(self):
        print("I am a teacher.")



student =Student()
graduate= GraduateStudent()
teacher =Teacher()

student.introduce()
graduate.introduce()
teacher.introduce()