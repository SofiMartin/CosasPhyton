from mundo_pc.dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return(f'Id: {self.id_teclado}, Marca: {self.marca}',
                f'Tipo de entrada: {self.tipo_entrada}')

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)  # Id: 1, Marca: HP, Tipo de teclado
    teclado2 = Teclado('Dell', 'USB')
    print(teclado2)  # Id: 2, Marca: Dell, Tipo de teclado
