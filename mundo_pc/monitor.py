class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio

    def __str__(self):
        return f'Id: {self.__id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'

if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    print(monitor1)
    monitor2 = Monitor('Dell', 17)