class Person:
    #El constructor tiene un nombre especifico
    def __init__(self,name,surname,age): # entre parentesis van todos los parametros que usaremos para definir el constructor
                #   El primero siempre apunta a si mismo y por costumbre se llama 'self'    
        self.name = name
        self.surname = surname
        self.age = age
        self.alive = True

    def full_name(self): # los metodos siempre llevan un parametro
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname} , {self.age}'