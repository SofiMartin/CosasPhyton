class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado de la suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado de la Resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado de la multiplicación {resultado}')

    def division(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado de la Division: {resultado}')

# Programa principal
if __name__ == '__main__':
    print('***Ejemplo Clase aritmetica***')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.division()
    aritmetica1.multiplicar()
    #Segundo Objeto
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()            
                 