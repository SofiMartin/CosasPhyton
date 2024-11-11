class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Sobreescribir el metodo __str__
def __str__(self): #Regresa una cadena
    return f'''Persona:
    nombre = {self.nombre}
    apellido = {self.apellido}'''

#Código principal
persona1 = Persona('Ana', 'Martínez')
print(persona1)  # El método __str__ se llama automaticamente en el Print
print(persona1.__str__()) #Esto es opcional
