class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

#Tambien se utiliza para conectar la base de datos.

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='uft8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
#TrazaError: toda la lista de errores si es que acurrió alguno.
#La firma del método son los parámetros que debemos agregar, de lo contrario marca error
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()
