#!C:\Users\zx22student3208\AppData\Local\Programs\Python\Python311\python.exe


from person import Person
from student import Student
from profesor import Profesor

#   How create a object
per1 = Person('Juan','Rodriguez Garcia',33)



print('Content-type: text/plain\n')

print(per1) #   Si tienes la clase __str__ creada en person.py (toString en java)

#   Modificar un atributo de un objeto
per1.name = "Paco"

print(f'{per1.name} {per1.surname}')

#   How create a object
per2 = Person('Ana','Lopez Garcia',43)


#per2.alive = False
if (per2.alive):
    print(per2.full_name())
else:
    print('Dead lol')



student1 = Student("Jose","Garcia Garcia", 18, "DAW")
print(student1)


profesor1 = Profesor("Alberto","Turienzo", 40)
profesor1.addAsignatura("Servidor")
profesor1.addAsignatura("Cliente")
print(profesor1)


for asig in profesor1.listaAsignaturas():
    print(asig)

print(student1.grade_name())