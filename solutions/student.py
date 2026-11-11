class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        # Проверяем, что оценка целое число от 2 до 5
        if not isinstance(grade, int) or not (2 <= grade <= 5):
            raise ValueError
        
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average(self, subject=None):
        if subject is None:
            all_grades = []
            for grades_list in self.grades.values():
                all_grades.extend(grades_list)
            
            if not all_grades:
                return 0.0
            return sum(all_grades) / len(all_grades)
        else:
            if subject not in self.grades:
                raise KeyError
            subject_grades = self.grades[subject]
            return sum(subject_grades) / len(subject_grades)

    def subjects(self):
        return sorted(list(self.grades.keys()))

    def debts(self):
        debt_subjects = []
        for subject in self.grades:
            if self.average(subject) < 3:
                debt_subjects.append(subject)
        return sorted(debt_subjects)

    def __lt__(self, other):
        return self.average() < other.average()

    def __repr__(self):
        return f"Student('{self.name}', {self.average():.2f})"


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add(self, student):
        if not isinstance(student, Student):
            raise TypeError
        
        for s in self.students:
            if s.name == student.name:
                raise ValueError
        
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def __contains__(self, student_name):
        for s in self.students:
            if s.name == student_name:
                return True
        return False

    def ranking(self):
        return sorted(self.students, key=lambda x: (-x.average(), x.name))

    def with_debts(self):
        debtors = []
        for s in self.students:
            if len(s.debts()) > 0:
                debtors.append(s.name)
        return sorted(debtors)

