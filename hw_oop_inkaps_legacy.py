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
        
    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self.grades.values()} 
Курсы в процессе изучения: {', '.join(self.courses_in_progress)} 
Завершенные курсы: {', '.join(self.finished_courses)}
        """
        return result

a = f''       

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname, gender):
       self.lect_grades = {}
       self.courses_attached = []

    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка за лекции: """
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
                
prep = Lecturer('Имя', 'Фамилие', 'lect_gender')
                
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['SQL']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_lecturer = Lecturer('Cool', 'Mentor', 'lect_gender')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
cool_reviewer.rate_hw(best_student, 'GIT', 8)

best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'JS', 9)
 
print(best_student.grades)
print()
print(cool_lecturer.lect_grades)
print()
print(best_student)
print()
print(cool_reviewer)
# print()
# print(cool_lecturer)