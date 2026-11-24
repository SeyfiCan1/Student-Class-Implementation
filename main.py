class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, student_id, gpa):
        super().__init__(name, age)
        self.student_id = student_id
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa


class Professor(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self):
        print(self.name, "is teaching.")


student = Student("Ahmet", 21, "S102", 3.25)
professor = Professor("Mehmet", 42, "Doctor")

print("Student Name:", student.name)
print("Student Age:", student.get_age())
print("Student GPA:", student.get_gpa())

print("Professor Name:", professor.name)
print("Professor Age:", professor.get_age())

professor.teach()
