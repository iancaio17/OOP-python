from modelos.restaurantes import Restaurante

restaurante_italiano = Restaurante('bonzini', 'italiano')
restaurante_japones = Restaurante('shoyo', 'japones')
restaurante_mexicano = Restaurante('nacho', 'mexicano')

restaurante_italiano.receber_avaliacao('Gui', 10)
restaurante_italiano.receber_avaliacao('Lais', 8)
restaurante_italiano.receber_avaliacao('Jorge', 6)

restaurante_mexicano.receber_avaliacao('Emy', 3)
restaurante_mexicano.receber_avaliacao('Luis', 4)
restaurante_mexicano.receber_avaliacao('Pedro', 10)

restaurante_japones.receber_avaliacao('Joao', 9)
restaurante_japones.receber_avaliacao('Jose', 5)
restaurante_japones.receber_avaliacao('Gustavo', 7)

restaurante_japones.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()