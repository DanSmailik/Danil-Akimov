class Student:

    group = "B29234"
    education = "Itstep"
    teacher = "Evgeniy"

    def __init__(self):
        print(id(self))

st1 = Student()
print(id(st1))

print(Student.group)