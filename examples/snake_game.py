import random
import time



serpiente_simbolo = "O"
# base_symbol = "\u2B1A"
relleno = "#"
valor_maximo = 20
comida_simbolo = "."
intervalo_tiempo = 1
matrix = [[]]
comida_posicion = [0,0]


def hacer_matrix():
    """ Crear una matrix de dimensiones n por n, donde n es igual al valor_maximo"""
    global matrix, base_symbol, max_value
    matrix = [[relleno for i in range(valor_maximo)] for i in range(valor_maximo)]
    # matrix = []
    # for linea_roja in range(max_value):
    #    matrix.append([])
    #    for linea_azul in range(max_value):
    #        linea_roja.append(base_symbol)

def imprimir_matrix():
    """imprimir cada lista y contenido de lista omitiendo los corchetes y comillas usando la función print con asterisco"""
    global matrix
    for __line in matrix:
        print(*__line)


def comida():
    """define una posicion aleatoria de la comida dentro de la matrix"""
    global matrix, valor_maximo, comida_simbolo, comida_posicion
    x = random.randint(0, valor_maximo -1)
    y = random.randint(0, valor_maximo -1)
    comida_posicion = [x,y]
    matrix[x][y] = comida_simbolo

class taza():
    """ejemplo de un objeto taza en la vida real"""
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
    """ Objeto serpiente del juego"""
    def __init__(self):
        """valores con los que inicia el objeto serpiente, como la posicion aleatoria y el sentido"""
        x = random.randint(0, valor_maximo -1)
        y = random.randint(0, valor_maximo -1)
        self.cuerpo = [[x,y]]
        self.sentido = 3

    def cabeza(self):
        """devuelve el primer valor de la  lista cuerpo"""
        return self.cuerpo[0]

    def longitud(self):
        """devuelve el tamaño de la lista cuerpo"""
        return self.cuerpo.__len__()


def print_serpiente(player):
    """agrega los puntos [y,x] de la lista cuerpo en el objeto serpiente y los pone dentro de matrix"""
    global serpiente_simbolo, matrix
    for point in player.cuerpo:
        matrix[point[0]][point[1]] = serpiente_simbolo


def limite(numero):
    """cuando el valor es cero devuelve el maximo para que la serpiente no choque con los limites, igualmente cuando el valor es maximo lo vuelve cero"""
    global valor_maximo
    if numero < 0:
        return valor_maximo -1
    elif numero > valor_maximo -1:
        return 0
    else:
        return numero

def move_serpiente(player):
    """define el movimiento de la serpiente en la dirección o sentido del objeto serpiente"""
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

def cambiar_direccion(serpiente):
    direccion = input("cambiar direccion")
    if direccion == '3':
        serpiente.sentido = 3
    elif direccion == '6':
        serpiente.sentido = 6
    elif direccion == '9':
        serpiente.sentido = 9
    elif direccion == '0':
        serpiente.sentido = 0
    else:
        print("error, presione una tecla: ")


def game():
    """inicia el juego con la secuencia de funciones para que funcione"""
    player1 =  serpiente()

    while True:
        time.sleep(intervalo_tiempo)
        print("size:",matrix.__len__(), " head:", player1.cabeza())
        hacer_matrix()
        # comida()
        print_serpiente(player1)
        move_serpiente(player1)
        imprimir_matrix()
        cambiar_direccion(player1)


game()
