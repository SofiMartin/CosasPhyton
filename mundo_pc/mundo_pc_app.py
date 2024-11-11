from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


print('*** Mundo PC ***')

#Computadora1
teclado1 = Teclado("HP", "USB")
raton1 = Raton("Logitech", "USB")
monitor1 = Monitor("Samsung", 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
print(computadora1)

#Computadora2
teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
print(computadora2)


# Crear la lista de computadora
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

teclado3 = Teclado('Dell', 'Bluetooth')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 24)
computadora3 = Computadora('Dell', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)
