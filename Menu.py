
import os
import funciones_nuevas

def menu_principal():
    print("1.Calculos numericos \n2.Tratamiento de String")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 3:
        print("Opcion incorrecta, ingrese nuevamente.")
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        menu_numerico()
    else:
        os.system ('cls')
        menu_string()

def menu_numerico():
    print("1.Multiplicacion \n2.Potencia \n3.Division \n4.Regresar")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 5:
        print("Opcion incorrecta, ingrese nuevamente.")
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        funciones_nuevas.multiplicacion()
    elif opcion == 2:
        funciones_nuevas.potencias()
    elif opcion == 3:
        funciones_nuevas.division()
    else:
        os.system ('cls')
        menu_principal()
    os.system ('cls')
    menu_numerico()

def menu_string():
    print("1.Palabra mas corta \n2.Palabra mas larga \n3.Cantidad de palabras \n4.Regresar")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 5:
        print("Opcion incorrecta, ingrese nuevamente.")
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        funciones_nuevas.string_corto()
    elif opcion == 2:
        funciones_nuevas.string_largo()
    elif opcion == 3:
        funciones_nuevas.cont_palabras()
    else:
        os.system ('cls')
        menu_principal()
        
    os.system ('cls')
    menu_string()
os.system ('cls')
menu_principal()
