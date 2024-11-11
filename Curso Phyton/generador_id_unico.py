from random import randint

print('*** Generador de Id Único***')

nombre = input('Cuál es tu nombre? ')
apellido = input('Cuál es tu apellido? ')
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY)? ')

#Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip().upper()[2:]  #También puede ser [2:4]

#Generar el valor aleatorio
aleatorio = randint(1000, 9999)

#Generamos el valor de id unico
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
      tu nuevo número de identificacion ID generado
      por el sistema es: {id_unico}
      felicidades!''')



