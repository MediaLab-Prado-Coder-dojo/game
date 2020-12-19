import random
import time
import keyboard
import os
from firebase import Firebase

"""iniciar base de datos en tiempo real firebase"""
config = {
  "apiKey": "AIzaSyAMj8kS-gcfbBm4OxIQELj5_dXeje7z8Ks",
  "authDomain": "medialabprado-snakegame.firebaseapp.com",
  "databaseURL": "https://medialabprado-snakegame-default-rtdb.firebaseio.com/",
  "storageBucket": "gs://medialabprado-snakegame.appspot.com"
}



relleno = "\u25A2"
valor_maximo = 30
comida_simbolo = "\u25CE"
intervalo_tiempo = 1
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

def lista_a_txt():
    global matrix
    str_matrix = ""
    for __line in matrix:
        for _content in __line:
            str_matrix +=_content
            str_matrix += " "
        str_matrix += "\n"
    os.system('clear')
    print("score:",player1.longitud() -1, " head:", player1.cabeza(), " food:", comida_posicion)
    print(str_matrix)


def comida():
    """define una posicion aleatoria de la comida dentro de la matrix"""
    global matrix, valor_maximo, comida_simbolo, comida_posicion
    x = random.randint(0, valor_maximo -1)
    y = random.randint(0, valor_maximo -1)
    comida_posicion = [x,y]
    matrix[x][y] = comida_simbolo


def limite(numero):
    """cuando el valor es cero devuelve el maximo para que la serpiente no choque con los limites, igualmente cuando el valor es maximo lo vuelve cero"""
    global valor_maximo
    if numero < 0:
        return valor_maximo -1
    elif numero > valor_maximo -1:
        return 0
    else:
        return numero

class serpiente():
    """ Objeto serpiente del juego"""
    def __init__(self, controls=["w","a","s","d"], simbolo="\u25A6"):
        """valores con los que inicia el objeto serpiente, como la posicion aleatoria y el sentido"""
        x = random.randint(0, valor_maximo -1)
        y = random.randint(0, valor_maximo -1)
        self.cuerpo = [[x,y]]
        self.sentido = 3
        self.controls = controls
        self.symbol = simbolo
        self.nombre = "Ignacio"
        # self.symbol = "\u25A6"

    def cabeza(self):
        """devuelve el primer valor de la  lista cuerpo"""
        return self.cuerpo[0]

    def longitud(self):
        """devuelve el tamaño de la lista cuerpo"""
        return self.cuerpo.__len__()

    def borrar_serpiente(self):
        global matrix, relleno
        for point in self.cuerpo:
            matrix[point[0]][point[1]] = relleno

    def print_serpiente(self):
        """agrega los puntos [y,x] de la lista cuerpo en el objeto serpiente y los pone dentro de matrix"""
        global matrix
        for point in self.cuerpo:
            matrix[point[0]][point[1]] = self.symbol

    def move_serpiente(self):
        """define el movimiento de la serpiente en la dirección o sentido del objeto serpiente"""
        y = self.cabeza()[0]
        x = self.cabeza()[1]
        if self.sentido == 0:
            self.cuerpo.insert(0, [limite(y-1), x])
        elif self.sentido == 3:
            self.cuerpo.insert(0,[y, limite(x+1)])
        elif self.sentido == 6:
            self.cuerpo.insert(0,[limite(y+1), x])
        elif self.sentido == 9:
            self.cuerpo.insert(0,[y, limite(x-1)])
        if self.cabeza() != comida_posicion:
            self.cuerpo.remove(self.cuerpo[-1])
        else:
            comida()

    def cambiar_direccion_kb(self):
        if keyboard.is_pressed(self.controls[0]):
            self.sentido = 0
        elif keyboard.is_pressed(self.controls[1]):
            self.sentido = 9
        elif keyboard.is_pressed(self.controls[2]):
            self.sentido = 6
        elif keyboard.is_pressed(self.controls[3]):
            self.sentido = 3


def multiplayer(players):
    for player in players:
        player.print_serpiente()
    imprimir_matrix()
    # lista_a_txt()
    for player in players:
        player.borrar_serpiente()
        player.move_serpiente()
        player.cambiar_direccion_kb()


def base_de_datos(player):
    firebase = Firebase(config)
    db = firebase.database()
    # data to save
    datos = {
        player.nombre : player.cuerpo
    }
    # Pass the user's idToken to the push method
    results = db.child("players").push(datos)

player1 = serpiente(simbolo="1")
player2 = serpiente(controls=["8","4","5","6"], simbolo="2")
# player3 = serpiente(controls=[])
players = [player1, player2]



def game():
    global players
    """inicia el juego con la secuencia de funciones para que inicie"""
    hacer_matrix()
    comida()

    while True:
        # print("score:",player1.longitud() -1, " head:", player1.cabeza(), " food:", comida_posicion)
        multiplayer(players)
        base_de_datos(player1)
        # player1.print_serpiente()
        # imprimir_matrix()
        # player1.borrar_serpiente()
        # player1.move_serpiente()
        # player1.cambiar_direccion_kb()
        time.sleep(intervalo_tiempo)

game()
