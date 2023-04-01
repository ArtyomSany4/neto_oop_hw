class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, lect_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [lect_grade]
            else:
                lecturer.lect_grades[course] = [lect_grade]
        else:
            return 'Ошибка'    

    def calculate_avrg_lect_estimete(self):
        total_grade = 0
        lenght = 0
        if len(self.grades) == 0:
            avrg_grade = 'Оценок еще не ставили!'
        else: 
            for v in self.grades.values():
                lenght += len(v)
                for el in v:
                    total_grade += el
            avrg_grade = total_grade / lenght
        return avrg_grade    


    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self.calculate_avrg_lect_estimete()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)} 
Завершенные курсы: {', '.join(self.finished_courses)}
        """
        return result



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
        
   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lect_grades = {}
        self.courses_attached = []

    def calculate_avrg_lect_estimete(self):
        total_grade = 0
        lenght = 0
        if len(self.lect_grades) == 0:
            avrg_grade = 'Оценок еще не ставили!'
        else: 
            for v in self.lect_grades.values():
                lenght += len(v)
                for el in v:
                    total_grade += el
            avrg_grade = float(total_grade / lenght)
        return avrg_grade    
    
    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calculate_avrg_lect_estimete()}
    """
        return result

# Заводим функцию сравнения лекторов и студентов по средней оценке
# Делаю для лектора -> self тут лектор
    def __lt__(self, other):
        if not isinstance(other, Student):
            err = 'Что-то пошло не так. Сравнить можно только лекторов и студентов по средней оценке!'
            return err
        return self.calculate_avrg_lect_estimete() < other.calculate_avrg_lect_estimete()

# при переназначении __lt__ работает только <, пришлось переназначать и __gt__.
# почему так, не разобрался. в уроке переназначали только lt
    def __gt__(self, other):
        if not isinstance(other, Student):
            err = 'Что-то пошло не так. Сравнить можно только лекторов и студентов по средней оценке!'
            return err
        return self.calculate_avrg_lect_estimete() > other.calculate_avrg_lect_estimete()


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
        result = f'Имя: {self.name} \nФамилия: {self.surname}'
        return result


# 1. для подсчета средней оценки за домашние задания по всем студентам в рамках
# конкретного курса (в качестве аргументов принимаем список студентов и название курса);
def calculate_avrg_hw_estimete(student_list, course_name):
    total_hw_grade = 0
    count = 0
    for student in student_list:
        if len(student.grades) > 0:
            if course_name in student.grades.keys():
                total_hw_grade += sum(student.grades[course_name])
                count += len(student.grades[course_name])
    if count == 0:
        result = 'По указанному списку и курсу совпадений нет!'
    else:
        result = f'Средняя оценка за ДЗ по всем студентам по курсу {course_name}: {total_hw_grade/count}'
    return result 

# 2. для подсчета средней оценки за лекции всех лекторов в рамках курса 
# (в качестве аргумента принимаем список лекторов и название курса)
def calculate_avrg_grade_all_lect(lect_list, course_name):
    total_lect_grade = 0
    count = 0
    for lect in lect_list:
        if len(lect.lect_grades) > 0:
            if course_name in lect.lect_grades.keys():
                total_lect_grade += sum(lect.lect_grades[course_name])
                count += len(lect.lect_grades[course_name])
    if count == 0:
        result = 'По указанному списку и курсу совпадений нет!'
    else:
        result = f'Средняя оценка за лекции списка лекторов по курсу {course_name}: {total_lect_grade/count}'
    return result    


# Создайте по 2 экземпляра каждого класса

# Создаем первого студента и накидываем ему курсов 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['SQL']
# Создаем второго студента и накидываем ему курсов 
scnd_student = Student('Second', 'Student', 'your_gender')
scnd_student.courses_in_progress += ['Проджект-менеджер', 'Python']
scnd_student.courses_in_progress += ['DATA science']
scnd_student.finished_courses += ['Арифметика']

# Создаем первого ревьюера и ему курсов
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['DATA science']
cool_reviewer.courses_attached += ['GIT']
# Создаем второго ревьюера и ему курсов
scnd_reviewer = Reviewer('Second', 'Reviewer')
scnd_reviewer.courses_attached += ['Python']
scnd_reviewer.courses_attached += ['GIT', 'Арифметика']

# Создаем лектора и ему курс
cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']
# Создаем второго лектора и ему курсов
scnd_lecturer = Lecturer('Second', 'Lecturer')
scnd_lecturer.courses_attached += ['Python', 'SQL']



# вызовите все созданные методы

# ставим оценки лекторам за курсы
best_student.rate_lector(cool_lecturer, 'Python', 10)
scnd_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(scnd_lecturer, 'SQL', 2)

# ставим оценки за домашку студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
scnd_reviewer.rate_hw(best_student, 'Python', 9)
scnd_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(scnd_student, 'Python', 7)
scnd_reviewer.rate_hw(scnd_student, 'Python', 3)
cool_reviewer.rate_hw(best_student, 'Python', 5)
scnd_reviewer.rate_hw(best_student, 'GIT', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 8)


print('Сравниваем студента и лектора по средней оценке (больше):', best_student > cool_lecturer)
print('Сравниваем студента и лектора по средней оценке (меньше):', best_student < cool_lecturer)

# Принтуем все созданные экземпляры
print(f'Первый студент: {best_student}')
print(f'Второй студент: {scnd_student}')
print(f'Первый ревьюер: {cool_reviewer}')
print(f'Второй ревьюер: {scnd_reviewer}')
print(f'Первый лектор: {cool_lecturer}')
print(f'Второй лектор: {scnd_lecturer}')
# Функция подсчета средней оценки за домашние задания
print(calculate_avrg_hw_estimete([best_student, scnd_student], 'Python'))
# Функция подсчета средней оценки за лекции
print(calculate_avrg_grade_all_lect([cool_lecturer, scnd_lecturer], 'Python'))