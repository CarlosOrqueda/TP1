#################################################### String ############################################################

# Pide una cadena y la devuelve
def solicitar_texto():
    texto = input("Ingrese texto ")
    while texto == "" or texto.isalpha() == False:
        texto = input("Ingrese texto ")
    return texto


# Simplifica la cadena y devuelve una lista de palabras
def armar_cadena(texto):
    reemplazar = texto.maketrans(",;.", "   ")
    lista_de_palabras = texto.translate(reemplazar).lower().split()
    return lista_de_palabras


# Recibe una lista itera sobre la misma y devuelve una lista auxiliar y la palabra mas corta
def iterar_listas(lista_de_palabras):
    palabra_corta = lista_de_palabras[0]  # Asigno primera palabra de la lista a la variable
    lista_auxiliar = []
    for palabra in lista_de_palabras:
        if len(palabra_corta) == len(palabra):
            lista_auxiliar.append(palabra)
            palabra_corta = palabra
        elif len(palabra_corta) > len(palabra):
            del lista_auxiliar[::]
            palabra_corta = palabra
            lista_auxiliar.append(palabra_corta)
    return palabra_corta, lista_auxiliar


# Pide un texto y muestra la cant. de palabras que tiene
def cont_palabras():
    texto = solicitar_texto()
    cantidad_palabras = len(armar_cadena(texto))
    print("La cantidad de palabras en el texto es " + str(cantidad_palabras) + ",incluyendo numeros")


# Pide un Texto y muestra la o las palabras mas cortas y su longitud
def string_corta():
    texto = solicitar_texto()
    lista_de_palabras = armar_cadena(texto)
    palabra_corta, lista_auxiliar = iterar_listas(lista_de_palabras)
    print("La/s palabra/s mas corta/s es/son {}, incluyendo numeros y tiene {} caracteres.".format(
        str(lista_auxiliar), len(palabra_corta)))


#################################################### Calculos ##########################################################

# Pide valores , verifica que sean numeros y los devuelve
def solicitar_numeros():
    num1 = input("ingrese un numero ")
    num2 = input("ingrese un numero ")
    while not num1.isdigit() and num2.isdigit():
        num1 = input("ingrese un numero ")
        num2 = input("ingrese un numero ")
    num1 = int(num1)
    num2 = int(num2)
    return num1, num2


# Funcion para validar el cambio de signo en funciones de cálculo numerico, con variable booleana.
def cambio_de_resultado(num1="", num2=""):
    if num1 < 0 and num2 < 0:
        return False
    elif num1 < 0 or num2 < 0:
        return True


# Realiza todos las divisiones por resta
def division_aux(dividendo, divisor):
    dividendo, divisor = abs(dividendo, divisor)
    cociente = 0
    if dividendo <= divisor:
        while dividendo <= divisor:
            dividendo = dividendo * 10
        while dividendo >= divisor:
            dividendo -= divisor
    else:
        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1
    return cociente, dividendo


# Solicita numeros y muestra el resultado
def division():
    dividendo, divisor = solicitar_numeros()
    por_menos_uno = cambio_de_resultado(dividendo, divisor)
    if divisor == 0:
        return print("No se puede dividir por 0")
    cociente, resto = division_aux(dividendo, divisor)
    if por_menos_uno:
        cociente = -cociente
    print("La division es {} y el resto {}.".format(cociente, resto))
