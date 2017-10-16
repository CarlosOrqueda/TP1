

import funciones
import os

# opciones menu, devuelve un valor entero sin excepcion
def menu():
    opcion = 0
    os.system('cls')
    while opcion == 0:
        os.system('cls')
        try:
            print("Selecciona una opción")
            print("1 - Numérico")
            print("2 - Cadenas de carácteres")
            print("3 - Salir")
            opcion = int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
            input("Ingrese una tecla para continuar...")
    return opcion


# opciones menu num, devuelve un valor entero
def sub_menu_num():
    opcion = 0
    os.system("cls")
    while opcion == 0:
        os.system('cls')
        try:
            print("Selecciona una opción")
            print("1 - Multiplicación")
            print("2 - División y resto")
            print("3 - Potencia")
            print("4 - Volver al Menú principal")
            opcion = int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
            input("Ingrese una tecla para continuar...")
            os.system("cls")
    return opcion


# opciones menu let, devuelve un valor entero
def sub_menu_let():
    os.system("cls")
    opcion = 0
    while opcion == 0:
        
        try:
            print("Selecciona una opción")
            print("1 - Palabra mas Larga")
            print("2 - Palabra mas corta")
            print("3 - Contar Palabras")
            print("4 - Volver al Menú principal")
            opcion = int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
            input("Ingrese una tecla para continuar...")
            os.system("cls")
    return opcion


# Se pide el ingreso de una cadena, si solo es un entero no se considera.
def solicitar_cadena():
    cadena = ""
    while cadena == "":
        try:
            cadena = input("Ingrese una cadena de texto :")
            try:
                cadena = int(cadena)
                print("No se puede considerar la operación con solo numeros")
                cadena = ""
            except ValueError:
                cadena = cadena

        except ValueError:
            print("No ingreso una cadena..")
            input("Ingrese una tecla para continuar...")
            
    return cadena



# Indicador de la o las palabras mas larga y contador de sus caracteres.
# Se ingresan un String "frase".
'''La variable "listaLarga" devuelve un String de la o las palabras mas largas y "cantidadDeLetras" devuelve un String
de la cantidad de letras de la o las palabras.'''


def palabraMasLargaCantidadDeLetras(valor1):
    frase = valor1
    cantidadDeLetras = 0
    listaLarga = []
    reemplazar = frase.maketrans(",;.", "   ")
    listaDePalabras = frase.translate(reemplazar).lower().split()
    palabraMasLarga = listaDePalabras[0]
    listaLarga.append(palabraMasLarga)
    for palabra in listaDePalabras:
        if len(palabraMasLarga) == len(palabra) and palabraMasLarga != palabra:
            listaLarga.append(palabra)
        elif len(palabraMasLarga) < len(palabra):
            palabraMasLarga = palabra
            del listaLarga[:]
            listaLarga.append(palabraMasLarga)
    for cantidad in listaLarga:
        if cantidadDeLetras < len(cantidad):
            cantidadDeLetras = len(cantidad)

    mensaje = "La/s palabra/s mas larga/s es/son {}, incluyendo numeros y la cantidad de caracteres es {}.".format(
        listaLarga, cantidadDeLetras)
    return mensaje


# Indicador de la o las palabras mas corta y contador de sus caracteres.
'''Recibe el parametro valor1, se transforma en una lista con la conversion necesaria
y devuelve un string
'''


def string_corto(valor1):
    cadena = valor1
    outside = "  "
    inside = ".,;"
    trans = cadena.maketrans(".,;!", "    ")
    cadena = cadena.translate(trans)
    lista_cadena = cadena.split()
    palabra_corta = lista_cadena[0]
    lista_auxiliar = []
    for i in lista_cadena:
        if len(palabra_corta) > len(i):
            del lista_auxiliar[::]
            palabra_corta = i
            lista_auxiliar.append(palabra_corta)
        elif len(palabra_corta) == len(i):
            lista_auxiliar.append(i)
            palabra_corta = i
    cantidad = len(palabra_corta)
    palabras_cortas = str(lista_auxiliar)
    palabras_cortas_mensaje = "La/s palabra/s mas corta/s es/son {}, incluyendo numeros y tiene {} caracteres.".format(
        palabras_cortas, cantidad)
    return palabras_cortas_mensaje  # palabras_cortas


# Contador de palabras en una cadena.
'''Recibe el parametro valor1, se transforma en una lista con la conversion necesaria
y devuelve un string'''


def contar_cadena(valor1):
    cadena = valor1
    trans = cadena.maketrans(".,;!", "    ")
    cadena = cadena.translate(trans)
    lista_cadena = cadena.split()
    cantidad_palabras = len(lista_cadena)
    mensaje = "La cantidad de palabras en el texto es " + str(cantidad_palabras) + ",incluyendo numeros"

    return mensaje


# Division por resta.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string

def division(valor1, valor2):
    valorA = int(valor1)
    valorB = int(valor2)

    cociente = 0
    contadorDeDecimales = 0
    porMenosUno = False
    mensaje = ""
    if valorA < 0 or valorB < 0:
        porMenosUno = True
    valorA = abs(valorA)
    valorB = abs(valorB)
    if valorB != 0:
        if valorA == 0:
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
        elif valorA <= valorB and valorB % valorA == 0:
            while valorB >= valorA:
                valorB += -valorA
                cociente += 1
            resto = valorB
            if porMenosUno == True:
                cociente = -cociente
            cociente = 1 / cociente
        else:
            while valorA <= valorB:
                valorA = valorA * 10
                contadorDeDecimales += 1
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
            if porMenosUno == True:
                cociente = -cociente
            cociente = cociente / (10 ** contadorDeDecimales)
    else:
        mensaje = "No se puede dividir por 0"
        resto = ""
        cociente = ""
        return mensaje

    mensaje = "La division es {} y el resto {}.".format(cociente, resto)
    return mensaje


# Multiplicacion por suma.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string

def multiplicacion(valor1, valor2):
    valorA = int(valor1)
    valorB = int(valor2)
    suma = 0
    if valorA < 0 and valorB < 0 or valorA > 0 and valorB > 0:
        if valorA < 0 and valorB < 0:
            valorA = -valorA
            valorB = -valorB
        if valorA <= valorB:
            for i in range(0, valorA):
                suma += valorB
        elif valorA > valorB:
            for i in range(0, valorB):
                suma += valorA
    elif valorA < 0:
        if abs(valorA) < valorB:
            for i in range(valorA, 0):
                suma += valorB
            suma = -suma
        else:
            for i in range(0, valorB):
                suma += valorA
    else:
        if abs(valorB) < valorA:
            for i in range(valorB, 0):
                suma += valorA
            suma = -suma
        else:
            for i in range(0, valorA):
                suma += valorB
    mensaje = "La multiplicacion es " + str(suma)
    return mensaje


# Potencia por multiplicacion.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string


def potencias(valor1, valor2):
    valorA = int(valor1)
    valorB = int(valor2)
    multp = 1
    if valorA != 0 and valorB != 0:
        if valorA > 0 and valorB > 0:
            for i in range(0, valorB):
                multp = multp * valorA
        elif valorB < 0:
            for i in range(valorB, 0):
                multp = multp * valorA
            multp = 1 / multp
        elif valorA < 0:
            for i in range(0, valorB):
                multp = multp * valorA
    else:
        if valorA == valorB == 0:
            mensaje = "La base y el exponente no pueden ser 0 a la vez."
            return mensaje
        multp = 0
    mensaje = "La potencia es " + str(multp)
    return mensaje


# Se piden parametros enteros sin excepcion para las funciones con enteros


def solicitud(mensaje_1, mensaje_2):
    valor_1 = ""
    valor_2 = ""
    while valor_1 == "" and valor_2 == "":
        try:
            mensaje="Ingrese " + mensaje_1+": "
            mensaje_2="Ingrese "+ mensaje_2+": "
            valor_1 = int(input(mensaje))
            try:
                valor_2 = int(input(mensaje_2 ))
            except ValueError:
                print("Ingrese un valor valido, solo un numero")
                valor_1 = ""
                valor_2 = ""
        except ValueError:
            print("Ingrese un valor valido, solo un numero")
            valor_1 = ""
            valor_2 = ""
    return valor_1, valor_2


# Recibe 1 o 2 parametros y los imprime en ambos casos de funciones, tanto enteros como cadenas de texto


def imprimir(parametro_1="", parametro_2=""):
    print(parametro_1, parametro_2)


def opcion_submenu():
    opcion = 0
    while opcion == 0 or opcion>=3:
        
        try:
            print("1 - Continuar en este menú")
            print("2 - Ir al menú Principal")
            
            opcion = int(input("¿Quiere continuar operando?: "))
            os.system("cls")
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
            input("Ingrese una tecla para continuar...")
            os.system("cls")
    return opcion
##############################################





salir=False
while salir==False or continuar==2:
    
    opcion=menu()
    
    if opcion==1:
        continuar=1
        while continuar==1:
            opcion=sub_menu_num()
            if opcion==1:
                mensaje_1=str("un numero")
                mensaje_2=str("un numero")
                num_1, num_2=solicitud(mensaje_1, mensaje_2)
                producto=multiplicacion(num_1,num_2)
                imprimir(producto)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==2:
                mensaje_1=str("un dividendo")
                mensaje_2=str("un divisor")
                dividendo, divisor=solicitud(mensaje_1, mensaje_2)
                try:                 
                    cociente=division(dividendo, divisor)
                    imprimir(cociente)
                except:
                    mensaje=division(dividendo,divisor)
                    print(mensaje)
                    continuar=opcion_submenu()
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==3:
                mensaje_1=str("una base")
                mensaje_2=str("un exponente")
                base,exponente=solicitud(mensaje_1, mensaje_2)
                try:  
                    potencia=potencia(base,exponente)
                    imprimir(potencia)
                except:
                    mensaje =potencias(base,exponente)
                    print(mensaje)
                    continuar=opcion_submenu()
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==4:
                #opcion=1
                continuar=0
                #salir=0
                #continuar=1
    elif opcion==2:
        continuar=1
        while continuar==1:
            opcion=sub_menu_let()
            if opcion==1:
                cadena=solicitar_cadena()
                cadena=palabraMasLargaCantidadDeLetras(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==2:
                cadena=solicitar_cadena()
                cadena=string_corto(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==3:
                cadena=solicitar_cadena()
                cadena=contar_cadena(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==4:
                continuar=0
                #salir=0
                            
        
    elif opcion==3:
        print("Saliendo")
        salir=True
        continuar=0
            
    else:
        print("No deberia llegar acá")
        





