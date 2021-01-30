import math

def vol_cubo(base):
    return base ** 3

def vol_cilindro(radio, altura):
    return (math.pi * (radio ** 2) * altura)

def vol_piramide_rectangular(base, altura):
    return (base * altura) / 3
