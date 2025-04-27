class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'Student with name: {self.name},class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name},subject: {self.subject}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers)+101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('-------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        return 'All Done for now'


# sushmoy = Student('Sushmoy Nandi', 9, 1)
# bappi = Teacher('Bappi', 'Algorithm', 101)
# print(sushmoy)
# print(bappi)
sushmoy = School('Akij Collegiate School')
sushmoy.enroll('sushmoy', 5200)
sushmoy.enroll('Bappi', 8000)
sushmoy.enroll('sushmoy1', 7000)
sushmoy.enroll('sushmoy2', 90000)

sushmoy.add_teacher('AAA', 'Algo')
sushmoy.add_teacher('BBB', 'DS')
sushmoy.add_teacher('CCC', 'Database')
print(sushmoy)
