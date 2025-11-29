class Class:
    def __init__(self, name):
        self.class_name = name
        self.students = {}

    def add_student(self, student: str, grade : float):
        self.student = student
        self.grade = grade
        self.students[student] = grade

    def get_average_grade(self) :
        sum_st = 0
        for student in self.students:
            sum_st += self.students[student]

        average = sum_st / len(self.students)

        return average


    def __repr__(self):
        return f'The students in {self.class_name}: {", ".join([name for name, grade in self.students.items()])}. Average grade: {self.get_average_grade():.2f}.'


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
