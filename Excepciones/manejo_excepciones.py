
resultado = None

try:
    a = int(input('Primer número:'))
    b = int(input('Segundo número:'))
    resulado = a/b
    #10/0       #Una división entre 0 genera un error,#se puede probar con cualquier calculadora
except ZeroDivisionError as e:
#Palabra reservada Except, en otros lenguajes se conoce como Catch-.
    print(f'Ocurrio un error: {e}')
except TypeError as e:
    print(f'ocurrio un error: {e}')
except Exception as e:
    print(f'Ocurrió un error: {e}')


print(f'Resultado: {resultado}')
