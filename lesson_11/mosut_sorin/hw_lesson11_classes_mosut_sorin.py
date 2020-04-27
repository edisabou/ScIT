# %load stud_collection.py
from collections.abc import MutableMapping, Mapping, Iterable, Collection, Container, Sized


class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age, id(self)
        )

    def __str__(self):
        return '{} {} {}'.format(
            self.first_name, self.last_name, self.age)

class StudentsCollection:

    def __init__(self, students_list=None):
        self._students = list(students_list) if students_list else []

    def __iter__(self):
        return iter(self._students)

    def __getitem__(self, index):
        return self._students[index]

    def __len__(self):
        return len(self._students)

    def __contains__(self, item):
        for student_test in self._students:
            if str(student_test) == str(item):
                return True

students = [
    Student('John', 'Doe', 19),
    Student('Jack', 'Fluffy', 18),
    Student('Matthew', 'Wu', 19),
    Student('Heather', 'Rafferty', 19),
    Student('Randall', 'Blackdall', 20),
    Student('Marissa', 'Raynaud', 19),
    Student('Marlo', 'Ranbot', 19),
    Student('Sorin', 'Mosut', 37)
]

stud_collection = StudentsCollection(students)

abcs = [MutableMapping, Mapping, Iterable, Collection, Container, Sized]
for abc in abcs:
    print(
        'stud_collection is a {}: {}'.format(
            abc.__name__, isinstance(stud_collection, abc))
    )

print('\n','Lenght of stud_colection: ',len(stud_collection),'\n')

student_test_1 = Student('Matthew', 'Wu', 19)
print(student_test_1 in stud_collection)
student_test_2 = Student('Ioan', 'Pop', 25)
print(student_test_2 in stud_collection)

