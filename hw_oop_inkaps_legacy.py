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

    def _avrg_estimate(self):
        total_grade = 0
        lenght = 0
        for v in self.grades.values():
            lenght += len(v)
            for el in v:
                total_grade += el
        avrg_grade = float(total_grade / lenght)
        return avrg_grade    

    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self._avrg_estimate()}
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

    def _lect_avrg_estimate(self):
        if len(self.lect_grades) == 0:
            avrg_grade = 'Оценок еще не ставили!'
        else:
            avrg_grade = sum(self.lect_grades.values(), [])

        return avrg_grade  

    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: {self._lect_avrg_estimate}
    """
        return result



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

# Создаем студента и накидываем ему курсов 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['SQL']

# создаем ревьюера и ему курсов
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

# создаем лектора и ему курс
cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

# создаем второго лектора
scnd_lecturer = Lecturer('Second', 'Lecturer')
scnd_lecturer.courses_attached += ['Python']

# ставим оценки за домашку студенту best_student
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
cool_reviewer.rate_hw(best_student, 'GIT', 8)

# ставим оценки лектору за курс
best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'JS', 9)

# ставим оценки второму лектору
best_student.rate_lector(scnd_lecturer, 'Python', 2)
 
print(best_student)
print(cool_reviewer)
print(scnd_lecturer)

