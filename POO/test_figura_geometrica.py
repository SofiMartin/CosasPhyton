from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(lado=-5, color='rojo')
print(f'Calculo area cuadrado: {cuadrado1.calcular_area}'())
print(cuadrado1)
#MRO - Method Resolution Order (Con un print nos dice el orden de nuestras clases)
#print(Cuadrado.__mro__)  #<class '__main__.Cuadrado'>

print('Creacion Objeto cuadrado'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=13, alto=8, color='verde')
print(f'Cálculo area rectángulo: {cuadrado1.calcular_area()}')
print(cuadrado1)