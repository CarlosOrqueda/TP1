def menu_principal():
    print("1.Calculos numericos \n2.Tratamineto de String")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 3:
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        menu_numerico()
    else:
        menu_string()

def menu_numerico():
    print("1.Multiplicacion \n2.Potencia \n3.Division \n4.Regresar")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 5:
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        multiplicacion()
    elif opcion == 2:
        potencia()
    elif opcion == 3:
        division()
    else:
        menu_principal()

def menu_string():
    print("1.Palabra mas corta \n2.Palabra mas larga \n3.Cantidad de palabras \n4.Regresar")
    opcion = int(input("Ingrese una opcion valida "))
    while opcion >= 5:
        opcion = int(input("Ingrese una opcion valida "))
    if opcion == 1:
        palabra_corta()
    elif opcion == 2:
        palabra_larga()
    elif opcion == 3:
        cant_palabras()
    else:
        menu_principal()

menu_principal()