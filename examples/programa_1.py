# import figuras
from areas import area_triangulo, area_cuadrado, area_circulo
# from figuras import *
from volumenes import vol_cubo, vol_cilindro, vol_piramide_rectangular

def inicio():
    print("Qué figura tienes?")
    eleccion = input("Menu: \n Triangulo 1, \n Cuadrado 2, \n Circulo 3, \n Cubo 4, \n Cilindro 5, \n Piramide 6 \n\n ")

    if eleccion == "1":
        base = float(input("Base: ? "))
        altura = float(input("Altura: ? "))
        resultado = area_triangulo(base, altura)

    # elif eleccion == "2":


    elif eleccion == "5":
        radio = float(input("Radio: ? "))
        altura= float(input("altura: ? "))

        resultado = vol_cilindro(radio, altura)

    print("el resultado es: " + str(resultado))
inicio()
