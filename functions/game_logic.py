def cambiar_direccion(sentido, tecla):
    cambio = sentido - tecla
    if cambio == 6:
        pass
    else:
        return tecla

def movimiento(serpiente, comida):
    if serpiente.sentido == 9:
        nueva_cabeza = [serpiente.cabeza[0] - 1,serpiente.cabeza[1]]
        serpiente.cuerpo.insert(0, nueva_cabeza)
        serpiente.cabeza = nueva_cabeza
        if comida != serpiente.cabeza:
            serpiente.cuerpo.remove((serpiente.cuerpo[-1]))
