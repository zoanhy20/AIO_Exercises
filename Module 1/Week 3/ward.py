from abc import ABC, abstractmethod


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.list_person = []

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.list_person:
            person.describe()

    def add_person(self, person: object):
        self.list_person.append(person)

    def count_doctor(self):
        count = 0
        for person in self.list_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.list_person.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        total_age_teachers = 0
        count_teachers = 0

        for person in self.list_person:
            if isinstance(person, Teacher):
                count_teachers += 1
                total_age_teachers += person.yob

        if count_teachers > 0:
            average_age_teachers = total_age_teachers / count_teachers
            return average_age_teachers

        return f"Don't have any teachers in {self.name}"


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name}, YOB: {self.yob}, Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name}, YOB: {self.yob}, Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name}, YOB: {self.yob}, Specialist: {self.specialist}")

# 2(a)


student1 = Student(name='studentA', yob=2010, grade='7')
student1.describe()

teacher1 = Teacher(name='teacherA', yob=1969, subject='Math')
teacher1.describe()

doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
doctor1.describe()

# 2(b)

teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')

ward1 = Ward(name='Ward1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)

print(f'Number of doctors: {ward1.count_doctor()}')

# 2(d)

print('After sorting Age of Ward1 people')
ward1.sort_age()
ward1.describe()

# 2(e)

print(f'Average age of teachers in {ward1.name}: {ward1.compute_average()}')
