class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''
    
#Código principal
if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("Logitech", "USB")
    monitor1 = Monitor("Samsung", 27)
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    
    teclado2 = Teclado('Gamer', 'Bluetooth')
    raton2 = Raton('Gamer', 'Bluetooth')
    monitor2 = Monitor('Gamer', 34)
    computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
    print(computadora2)