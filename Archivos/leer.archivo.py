archivo = open('prueba.txt', 'r', encoding='uft8') #abrir archivo, despues de Open se pone la ruta del archivo
#print(archivo.read())

#leer algunos caracteres
#print(archivo.read(5))

#Leer líneas completas
#print(archivo.readline())

#Iterar el archivo
# for linea in archivo:
#for linea in archivo:
#    print(linea)

#Leer lineas
#print(archivo.readlines)

#Acceder a una linea de la lista
#print(archivo.readlines()[1])

#Abrimos un nuevo archivo
#a = anexar informacion
archivo2 = open('copia.txt', 'a', encoding='uft8') #Si no existe lo crea
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
