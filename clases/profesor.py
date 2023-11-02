from person import Person

class Profesor(Person):
    def __init__(self, name, surname, age):
        Person.__init__(self, name, surname, age)
        self.asignaturas = []
    
    def __str__(self):
        return  f'{self.name} {self.surname} , {self.age}, profesor'
    
    def listaAsignaturas(self):
        return self.asignaturas
    
    def addAsignatura(self, nombreAsig):
        self.asignaturas.append(nombreAsig)