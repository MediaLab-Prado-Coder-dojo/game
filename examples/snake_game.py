import random
import time


serpiente_simbolo = "\u25A2"
# base_symbol = "\u2B1A"
relleno = "."
valor_maximo = 3
comida_simbolo = "\u2586"
intervalo_tiempo = 1
matrix = [[]]
comida_posicion = [0,0]


def hacer_matrix():
    global matrix, base_symbol, max_value
    matrix = [[relleno for i in range(valor_maximo)] for i in range(valor_maximo)]
    # matrix = []
    # for linea_roja in range(max_value):
    #    matrix.append([])
    #    for linea_azul in range(max_value):
    #        linea_roja.append(base_symbol)

def imprimir_matrix():
    global matrix
    for __line in matrix:
        print(*__line)


def comida():
    global matrix, valor_maximo, comida_simbolo, comida_posicion
    x = random.randint(0, valor_maximo -1)
    y = random.randint(0, valor_maximo -1)
    comida_posicion = [x,y]
    matrix[x][y] = comida_simbolo

class taza():
    def __init__(self):
        self.contenido = "nada"
        self.color = "rojo"
        self.tamaño = 7
    
    def checar_contenido(self):
        return self.contenido

    def rellenar_con_cafe(self):
        self.contenido = "cafe"
        return "tiene cafe"

    def vaciar(self):
        self.contenido = "nada"
        return "se ha vaciado"


class serpiente():
    def __init__(self):
        x = random.randint(0, valor_maximo -1)
        y = random.randint(0, valor_maximo -1)
        self.cuerpo = [[x,y]]
        self.sentido = 3

    def cabeza(self):
        return self.cuerpo[0]

    def longitud(self):
        return self.cuerpo.__len__()


def print_serpiente(player):
    global serpiente_simbolo, matrix
    for point in player.cuerpo:
        matrix[point[0]][point[1]] = serpiente_simbolo


def limite(numero):
    global valor_maximo
    if numero < 0:
        return valor_maximo -1
    elif numero > valor_maximo -1:
        return 0
    else:
        return numero

def move_serpiente(player):
    y = player.cabeza()[0]
    x = player.cabeza()[1]

    if player.sentido == 0:
        player.cuerpo.insert(0, [limite(y-1), x])
    elif player.sentido == 3:
        player.cuerpo.insert(0,[y, limite(x+1)])
    elif player.sentido == 6:
        player.cuerpo.insert(0,[limite(y+1), x])
    elif player.sentido == 9:
        player.cuerpo.insert(0,[y, limite(x-1)])

    if player.cabeza() != comida_posicion:
        player.cuerpo.remove(player.cuerpo[-1])
    else:
        comida()

def game():
    player1 =  serpiente()

    while True:
        time.sleep(intervalo_tiempo)
        print("size:",matrix.__len__(), " head:", player1.cabeza())
        hacer_matrix()
        comida()
        print_serpiente(player1)
        move_serpiente(player1)
        imprimir_matrix()


game()
