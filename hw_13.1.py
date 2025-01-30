class CustomError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        if self.gender == "Male":
            return f"{self.first_name} {self.last_name} is {self.age} y.o. He is {self.gender}"
        else:
            return f"{self.first_name} {self.last_name} is {self.age} y.o. She is {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender , age , first_name , last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise CustomError("В групі має бути не більше 10 студентів")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)


    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


students = [
        Student('Male', 30, 'Steve', 'Jobs', 'AN142') ,
        Student('Female', 25, 'Liza', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza1', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza2', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza3', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza4', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza5', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza6', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza7', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza8', 'Taylor', 'AN145') ,
        Student('Female', 25, 'Liza9', 'Taylor', 'AN145')
]

gr = Group('PD1')

for stud in students:
        try:
            gr.add_student(stud)
        except Exception as e:
            print(f"Error {e}")
            break

print(gr)
assert str(gr.find_student('Jobs')) == str(students[0]), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
