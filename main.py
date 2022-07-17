class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calc_avg(self):
        total = 0
        if len(self.grades) != 0:
            for course, hw_grades in self.grades.items():
                course_avg_grade = sum(hw_grades) / len(hw_grades)
                total += course_avg_grade
            avg_grade = round(total / len(self.grades), 2)
        else:
            avg_grade = 0
        return avg_grade

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and 0 < grade <= 10:
            if course in lecturer.lecture_rates:
                lecturer.lecture_rates[course] += [grade]
            else:
                lecturer.lecture_rates[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print("Имя: ", self.name)
        print("Фамилия: ", self.surname)
        print("Средняя оценка за домашние задания: ", self.calc_avg())
        print("Курсы в процессе изучения: ", ", ".join(self.courses_in_progress))
        print("Завершенные курсы: ", ", ".join(self.finished_courses))
        return ' '

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calc_avg() < other.calc_avg()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_rates = {}

    def calc_avg(self):
        total = 0
        if len(self.lecture_rates) != 0:
            for lecture, rates in self.lecture_rates.items():
                course_avg_rate = sum(rates) / len(rates)
                total += course_avg_rate
            avg_rate = round(total / len(self.lecture_rates), 2)
        else:
            avg_rate = 0
        return avg_rate

    def __str__(self):
        print("Имя: ", self.name)
        print("Фамилия: ", self.surname)
        print("Средняя оценка за лекции:", self.calc_avg())
        return ' '

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calc_avg() < other.calc_avg()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print("Имя: ", self.name)
        print("Фамилия: ", self.surname)
        return ' '


def calc_hw_avg(students, course):
    total = 0
    for student in students:
        if course in student.grades:
            student_avg = sum(student.grades[course]) / len(student.grades[course])
            total += student_avg
    hw_avg = total / len(students)
    return hw_avg


def calc_lecture_avg(lecturers, course):
    total = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            lecturer_avg = sum(lecturer.lecture_rates[course]) / len(lecturer.lecture_rates[course])
            total += lecturer_avg
    lecture_avg = total / len(lecturers)
    return lecture_avg


student1 = Student('Ruoy', 'Eman', 'woman')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Vasya', 'Pupkin', 'man')
student2.courses_in_progress += ['Python', 'Git']


reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Введение в программирование']
reviewer2 = Reviewer('Some', 'Guy')
reviewer2.courses_attached += ['Git']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Python', 10)


lecturer1 = Lecturer('Tom', 'Hiddleston')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Tom', 'Hardy')
lecturer2.courses_attached += ['Git']
student1.rate_lecture(lecturer1, 'Git', 5)
student2.rate_lecture(lecturer1, 'Git', 10)
student1.rate_lecture(lecturer2, 'Git', 8)

print(student1.grades)
print(student2.grades)
print(student1)
print(student2)
print("student1 < student2: ", student1 < student2)

print(lecturer1.lecture_rates)
print(lecturer2.lecture_rates)
print(lecturer1)
print(lecturer2)
print("lecturer1 < lecturer2: ", lecturer1 < lecturer2)

print(reviewer1)
print(reviewer2)

print("Python homework average grade: ", calc_hw_avg([student1, student2], 'Python'))
print("Git lecture average rate: ", calc_lecture_avg([lecturer1, lecturer2], 'Git'))