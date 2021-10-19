class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_rate(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):
        sum = 0
        count = 0
        for value in self.grades.values():
            for item in value:
                sum = sum + int(item)
                count += 1
            result = round((sum / count), 2)
        return result

    def __lt__(self, student):
        if not isinstance(student, Student):
            return
        return self.middle_grade() < student.middle_grade()

    def __str__(self):
        progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        middle = self.middle_grade()
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {middle}\nКурсы в процессе изучения: {progress}\nЗавершенные курсы: {finished}')
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            return
        return Student.middle_grade(self) < Student.middle_grade(lecturer)

    def __str__(self):
        middle = Student.middle_grade(self)
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {middle}')
        return result


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return result


def student_middle_rate(students_list, course):
    n = 0
    x = 0
    for student in students_list:
        if course in student.grades:
            for i in student.grades[course]:
                x = x + int(i)
                n += 1
    x = round((x / n), 2)
    return x


def lecturer_middle_rate(lecturers_list, course):
    n = 0
    x = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            for i in lecturer.grades[course]:
                x = x + int(i)
                n += 1
    x = round((x / n), 2)
    return x
first_student = Student('Bob', 'Dow', 'm')
first_student.courses_in_progress += ['Git']
first_student.courses_in_progress += ['JS']
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Go']
first_student.finished_courses += ['PHP']
second_student = Student('John', 'Dow', 'm')
second_student.courses_in_progress += ['Git']
reviewer = Reviewer('Some', 'Bob')
reviewer.courses_attached += ['Git']
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Kotlin']
reviewer.courses_attached += ['JS']
reviewer.rate_hw(first_student, 'Python', 8)
reviewer.rate_hw(first_student, 'Git', 8)
reviewer.rate_hw(first_student, 'Git', 5)
reviewer.rate_hw(first_student, 'Kotlin', 7)
reviewer.rate_hw(first_student, 'JS', 3)
reviewer.rate_hw(first_student, 'JS', 4)
first_lecturer = Lecturer('Bob', 'Bobbins')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Go']
first_student.lecturer_rate(first_lecturer, 'Python', 4)
first_student.lecturer_rate(first_lecturer, 'Go', 7)
first_student.lecturer_rate(first_lecturer, 'Python', 4)
first_student.lecturer_rate(first_lecturer, 'Go', 7)
reviewer.rate_hw(second_student, 'Git', 7)
second_lecturer = Lecturer('John', 'Bobbins')
second_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Python']
second_student.lecturer_rate(second_lecturer, 'Python', 4)
second_student.lecturer_rate(second_lecturer, 'Git', 9)
students_list = [first_student, second_student]
lecturers_list = [first_lecturer, second_lecturer]
student_mid_rate = student_middle_rate(students_list, 'Git')
lecturer_mid_rate = lecturer_middle_rate(lecturers_list, 'Python')

print(first_student)
print(second_student)
print(second_lecturer)
print(reviewer)
print(f'Средняя оценка за домашние задания по всем студентам: {student_mid_rate}')
print(f'Средняя оценка за лекции всех лекторов: {lecturer_mid_rate}')
print(
    f'Сравнение двух лекторов: {Student.middle_grade(second_lecturer)} < {Student.middle_grade(first_lecturer)} = {second_lecturer < first_lecturer}')
print(
    f'Сравнение двух студентов: {Student.middle_grade(first_student)} < {Student.middle_grade(second_student)} = {first_student < second_student}')

