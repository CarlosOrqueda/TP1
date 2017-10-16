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


# opciones submenu, devuelve un entero sin excepcion
def opciones_submenu():
    opcion = 0
    while opcion == 0:
        try:
            print("1 - Continuar")
            print("2 - Ir al menú")
            print("3 - Ir al menú principal")
            opcion = int(input("¿Quiere continuar operando?: "))
            os.system("cls")
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
            input("Ingrese una tecla para continuar...")
            os.system("cls")
    return opcion


def opcion_submenu():
    opcion = 0
    while opcion == 0 or opcion >= 3:

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


# Limpiador de String
def armar_cadena(texto):
    reemplazar = texto.maketrans(",;.", "   ")
    lista_de_palabras = texto.translate(reemplazar).lower().split()
    return lista_de_palabras


# Indicador de la o las palabras mas larga y contador de sus caracteres.
# Se ingresan un String "frase".
'''La variable "listaLarga" devuelve un String de la o las palabras mas largas y "cantidadDeLetras" devuelve un String
de la cantidad de letras de la o las palabras.'''


def palabra_mas_larga(lista_de_palabras):
    cantidad_de_letras = 0
    lista_larga = []
    palabra_mas_larga = lista_de_palabras[0]
    lista_larga.append(palabra_mas_larga)
    for palabra in lista_de_palabras:
        if len(palabra_mas_larga) == len(palabra) and palabra_mas_larga != palabra:
            lista_larga.append(palabra)
        elif len(palabra_mas_larga) < len(palabra):
            palabra_mas_larga = palabra
            del lista_larga[:]
            lista_larga.append(palabra_mas_larga)
    for cantidad in lista_larga:
        if cantidad_de_letras < len(cantidad):
            cantidad_de_letras = len(cantidad)

    mensaje = "La/s palabra/s mas larga/s es/son {}, incluyendo numeros y la cantidad de caracteres es {}.".format(
        lista_larga, cantidad_de_letras)
    return mensaje


# Indicador de la o las palabras mas corta y contador de sus caracteres.
'''Recibe el parametro valor1, se transforma en una lista con la conversion necesaria
y devuelve un string
'''


def string_corto(lista_de_palabras):
    palabra_corta = lista_de_palabras[0]
    lista_auxiliar = []
    for i in lista_de_palabras:
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


def contar_cadena(lista_de_palabras):
    cantidad_palabras = len(lista_de_palabras)
    mensaje = "La cantidad de palabras en el texto es " + str(cantidad_palabras) + ",incluyendo numeros"
    return mensaje


def cambio_de_resultado(num1="", num2=""):
    boolean=False
    if num1 < 0 and num2 < 0:
        boolean = False
    elif num1<0 or num2<0:
        boolean = True
    return boolean


# Division por resta.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string

def division(dividendo, divisor):
    cociente = 0
    por_menos_uno = cambio_de_resultado(dividendo, divisor)
    dividendo = abs(dividendo)
    divisor = abs(divisor)

    if divisor != 0:
        if dividendo == 0:
            resto = dividendo
        elif dividendo <= divisor:
            while dividendo <= divisor:
                dividendo = dividendo * 10
            while dividendo >= divisor:
                dividendo -= divisor
                cociente = 0
            resto = dividendo
        else:
            while dividendo >= divisor:
                dividendo -= divisor
                cociente += 1
            resto = dividendo

    else:
        mensaje = "No se puede dividir por 0"
        return mensaje
    if por_menos_uno:
            cociente = -cociente
    mensaje = "La division es {} y el resto {}.".format(cociente, resto)
    return mensaje


# Multiplicacion por suma.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string

def multiplicacion(multiplicando, multiplicador):
    suma = 0
    por_menos_uno = cambio_de_resultado(multiplicando, multiplicador)
    multiplicador = abs(multiplicador)
    multiplicando = abs(multiplicando)

    if multiplicando <= multiplicador:
        for i in range(0, multiplicando):
            suma += multiplicador
    else:
        for i in range(0, multiplicador):
            suma += multiplicando
    if por_menos_uno:
        suma = -suma
    mensaje = "La multiplicacion es " + str(suma)
    return mensaje


# Potencia por multiplicacion.
# Recibe el parametro valor1, valor2, ambos se castean, se opera y devuelve un string


def potencias(base, exponente):
    base2 = base
    exponente_negativo = cambio_de_resultado(abs(base2), exponente)
    multp = 1
    base = abs(base)
    exponente = abs(exponente)
    positivo=False
    if base != 0 and exponente != 0:
        if base2 < 0 and exponente % 2 == 0:
        
            positivo = True
        #elif exponente%2==0:
        #    positivo=False
        if exponente < base:
            for i in range(0, exponente):
                multp *= base
        else:
            for i in range(0, base):
                multp *= exponente
        if exponente_negativo:
            multp = 1 / multp
        elif positivo:
            multp = abs(multp)
    else:
        if base == exponente == 0:
            mensaje = "La base y el exponente no pueden ser 0 a la vez."
            return mensaje
        multp = 0
    mensaje = "La potencia es " + str(multp)
    return mensaje


# Se piden parametros enteros sin excepcion para las funciones con enteros
# Solo tiene pocos cambios, por comodidad mas que nada.


def solicitud(mensaje_1, mensaje_2):
    valor_1 = ""
    valor_2 = ""
    while valor_1 == "" and valor_2 == "":
        try:

            valor_1 = int(input(mensaje_1))
            try:
                valor_2 = int(input(mensaje_2))
            except ValueError:
                print("Ingrese un valor valido, solo un numero")
                valor_1 = ""
                valor_2 = ""
        except ValueError:
            print("Ingrese un valor valido, solo un numero")
            valor_1 = ""
            valor_2 = ""
    return valor_1, valor_2


def opcion_submenu():
    opcion = 0
    while opcion == 0 or opcion >= 3:

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


# Recibe 1 o 2 parametros y los imprime en ambos casos de funciones, tanto enteros como cadenas de texto


def imprimir(parametro_1="", parametro_2=""):
    print(parametro_1, parametro_2)
