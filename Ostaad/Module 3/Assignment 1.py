class Student:

    def __init__(self, name="Unknown", student_id="Not Assigned"):
        self.name = name
        self.student_id = student_id

    def display(self):
        print("Student Name :", self.name)
        print("Student ID   :", self.student_id)

    def future_feature(self):
        pass


student1 = Student()

student2 = Student("Ayshi", "221-15-4231")
student3 = Student("Rahim", "221-15-1001")

print("Student 1")
student1.display()

print("\nStudent 2")
student2.display()

print("\nStudent 3")
student3.display()