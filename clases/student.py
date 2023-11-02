from person import Person

class Student(Person):
    def __init__(self,name,surname,age,grade):
        Person.__init__(self,name,surname,age) # al llamar al constructor padre hay que pasarle el self
        self.grade = grade

    def __str__(self):
        return f'{self.name} {self.surname} , {self.age}, {self.grade}'
    
    def grade_name(self):
        return f'Esta estudiando {self.grade}'