try:
    archivo = open('prueba.txt', 'w', endcoding='uft8') #Soporta acentos en nuestro archivo
    archivo.write('Agregamos información al archivo')
    #archivo.write('Adios')
except Exception as e:
    print(f'Error al abrir el archivo: {e}')
finally:
    archivo.close()