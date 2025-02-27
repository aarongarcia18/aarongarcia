class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old, and I study {self.course}.")

student1 = Student("Aaron", 19, "Information Technology")
student2 = Student("Eljake", 24, "Engineering")
student3 = Student("Astrid", 20, "Tourism")

student1.introduce()
student2.introduce()
student3.introduce()
