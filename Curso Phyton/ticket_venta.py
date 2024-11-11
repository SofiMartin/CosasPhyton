print('*** Generación ticket Venta***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platano = float(input('Precio platanos: '))
descuento_porcentaje = int(input('Aplicar algún descuento (%)? '))

# Cálculo subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

#Cálculos con IVA (21%)
impuesto = subtotal_con_descuento *0.21

# Calculo total de la compra con impuestos
costo_total_compra = subtotal + impuesto

print(f'''
Subtotal: ${subtotal:2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto(21%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')