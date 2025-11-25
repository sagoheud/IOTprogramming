class Student:
    def __init__(self, name, grade, number):
        self.name = name
        self.grade = grade
        self.number = number

    def __repr__(self):
        return repr((self.name, self.grade, self.number))
    
students = [
Student("홍길동", 3, 15),
Student("김철수", 2, 10),
Student("이영희", 1, 5)
]

print(sorted(students, key=lambda student: student.grade))
print(sorted(students, key=lambda student: student.name))
print(sorted(students, key=lambda student: student.number))