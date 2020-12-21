from configuration import tamaño_campo


relleno = " "
comida_simbolo = "\u25CE"


def hacer_matrix(tamaño_campo):
    """ Crear una matrix de dimensiones n por n, donde n es igual al tamaño_campo"""
    global base_symbol
    return [[relleno for i in range(tamaño_campo)] for i in range(tamaño_campo)]


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


matrix = hacer_matrix(tamaño_campo)