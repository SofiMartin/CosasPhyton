from mundo_pc.dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        self.marca = marca
        self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada) #Buena práctica.

    def __str__(self):
        return f'Id: {self.id_raton}, Marca: {self.marca},
        Tipo de entrada: {self.tipo_entrada}'
    
#Código Principal
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Logitech', 'Bluetooth')
    print(raton2)
