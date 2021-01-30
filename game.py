import random
import time
import keyboard
import os
from firebase import Firebase
#librerias propias
from configuration import config, intervalo_tiempo, tamaño_campo, comida_posicion
from ascii import relleno, matrix, comida_simbolo, hacer_matrix, imprimir_matrix, lista_a_txt
from pygame_graficas import graficas


def comida(tamaño_campo):
    """define una posicion aleatoria de la comida dentro de la matrix"""
    global matrix, comida_simbolo, comida_posicion
    x = random.randint(0, tamaño_campo -1)
    y = random.randint(0, tamaño_campo -1)
    comida_posicion = [x,y]
    matrix[x][y] = comida_simbolo


def limite(numero):
    """cuando el valor es cero devuelve el maximo para que la serpiente no choque con los limites, igualmente cuando el valor es maximo lo vuelve cero"""
    global tamaño_campo
    if numero < 0:
        return tamaño_campo -1
    elif numero > tamaño_campo -1:
        return 0
    else:
        return numero


class serpiente():
    """ Objeto serpiente del juego"""
    def __init__(self, controls=["w","a","s","d"], simbolo="\u25A6", name="anonymous"):
        """valores con los que inicia el objeto serpiente, como la posicion aleatoria y el sentido"""
        x = random.randint(0, tamaño_campo -1)
        y = random.randint(0, tamaño_campo -1)
        self.bloques = [[x,y]]
        self.sentido = 3
        self.controls = controls
        self.symbol = simbolo
        self.nombre = name

    def cabeza(self):
        """devuelve el primer valor de la  lista.bloques"""
        return self.bloques[0]

    def longitud(self):
        """devuelve el tamaño de la lista.bloques"""
        return self.bloques.__len__()

    def borrar_serpiente(self):
        global matrix, relleno
        for point in self.bloques:
            matrix[point[0]][point[1]] = relleno

    def print_serpiente(self):
        """agrega los puntos [y,x] de la lista.bloques en el objeto serpiente y los pone dentro de matrix"""
        global matrix
        for point in self.bloques:
            matrix[point[0]][point[1]] = self.symbol

    def move_serpiente(self):
        """define el movimiento de la serpiente en la dirección o sentido del objeto serpiente"""
        y = self.cabeza()[0]
        x = self.cabeza()[1]
        if self.sentido == 0:
            self.bloques.insert(0, [limite(y-1), x])
        elif self.sentido == 3:
            self.bloques.insert(0,[y, limite(x+1)])
        elif self.sentido == 6:
            self.bloques.insert(0,[limite(y+1), x])
        elif self.sentido == 9:
            self.bloques.insert(0,[y, limite(x-1)])
        if self.cabeza() != comida_posicion:
            self.bloques.remove(self.bloques[-1])
        else:
            comida(tamaño_campo)

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


def setup_db(player):
    global db
    firebase = Firebase(config)
    db = firebase.database()
    results = db.child("players").child(player.nombre).set("started")


def base_de_datos(player):
    global db
    datos = {
        "bloques" : player.bloques,
        "sentido" : player.sentido,
        "score" : player.longitud(),
        "simbolo" : player.symbol
    }
    db.child("players").child(player.nombre).update(datos)


player1 = serpiente(simbolo="1", name="Ignacio")
player2 = serpiente(controls=["8","4","5","6"], simbolo="2", name="Homero")
# player3 = serpiente(controls=[])
players = [player1, player2]


def game():
    global players, tamaño_campo
    """inicia el juego con la secuencia de funciones para que inicie"""
    hacer_matrix(tamaño_campo)
    comida(tamaño_campo)
    setup_db(player1)
    setup_db(player2)
    while True:
        print("score:",player1.longitud() -1, " head:", player1.cabeza(), " food:", comida_posicion)
        multiplayer(players)
        base_de_datos(player1)
        base_de_datos(player2)
        time.sleep(intervalo_tiempo)
game()
