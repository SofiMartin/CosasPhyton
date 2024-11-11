print('Sistema de Empleados')
nombre_empleado = input('Nombre del empleado:')
edad_empleado = int(input('Edad del empleado:'))
salario_empleado = float(input('Salario del empleado:'))
es_jefe_departamento = input('Es jefe departamento (Si/No)?')

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

#Imprimir los valores del empleado
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado}')
print(f'Es jefe de Departamento? {es_jefe_departamento}')
