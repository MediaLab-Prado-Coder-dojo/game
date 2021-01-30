import random
import time
import keyboard


serpiente_simbolo = "O"
relleno = " "
valor_maximo = 20
comida_simbolo = "."
intervalo_tiempo = 0.2
matrix = [[]]
comida_posicion = [0,0]


def hacer_matrix():
    """ Crear una matrix de dimensiones n por n, donde n es igual al valor_maximo"""
    global matrix, base_symbol, max_value
    matrix = [[relleno for i in range(valor_maximo)] for i in range(valor_maximo)]


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


def borrar_serpiente(player):
    global matrix
    for point in player.cuerpo:
        matrix[point[0]][point[1]] = relleno


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


def cambiar_direccion_kb(serpiente):
    if keyboard.is_pressed('w'):
        serpiente.sentido = 0
    
    elif keyboard.is_pressed('s'):
        serpiente.sentido = 6
    
    elif keyboard.is_pressed('a'):
        serpiente.sentido = 9
    
    elif keyboard.is_pressed('d'):
        serpiente.sentido = 3


def game():
    """inicia el juego con la secuencia de funciones para que funcione"""
    player1 =  serpiente()
    hacer_matrix()
    comida()
    imprimir_matrix()
    while True:
        print("score:",player1.longitud() -1, " head:", player1.cabeza())
        print_serpiente(player1)
        imprimir_matrix()
        borrar_serpiente(player1)
        move_serpiente(player1)
        cambiar_direccion_kb(player1)
        time.sleep(intervalo_tiempo)
        
game()
