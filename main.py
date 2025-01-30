from module3 import Student
from module4 import Group

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
assert gr.find_student('Jobs') == students[0]
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
