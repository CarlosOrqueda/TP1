#################################################### String ############################################################

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


# Pide un Texto y muestra la o las palabras mas cortas y su longitud
def string_corto():
    texto = solicitar_texto()
    lista_de_palabras = armar_cadena(texto)
    palabra_corta, lista_auxiliar = iterar_listas(lista_de_palabras)
    print("La/s palabra/s mas corta/s es/son {}, incluyendo numeros y tiene {} caracteres.".format(
        str(lista_auxiliar), len(palabra_corta)))
    input("Presione una tecla para continuar...")


# Recibe una lista e itera para devolver una lista de palabras largas y la cantidad de caracteres
def iterar_palabras_largas(lista_de_palabras):
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
    print(len(lista_de_palabras[0]))
    cantidad_de_letras = len(lista_de_palabras[0])
    return lista_larga, cantidad_de_letras


# Solicita una cadena de texto y muestra la palabra/s mas largas y su cant. de letras.
def string_largo():
    texto = solicitar_texto()
    lista_de_palabras = armar_cadena(texto)
    lista_larga, cantidad_de_letras = iterar_palabras_largas(lista_de_palabras)
    palabras_largas = "La/s palabra/s mas larga/s es/son {}, incluyendo numeros y la cantidad de caracteres es {}.".format(
        lista_larga, cantidad_de_letras)
    print(palabras_largas)
    input("Presione una tecla para continuar...")
    return palabras_largas


# Pide un texto y muestra la cant. de palabras que tiene
def cont_palabras():
    texto = solicitar_texto()
    cantidad_palabras = len(armar_cadena(texto))
    print("La cantidad de palabras en el texto es " + str(cantidad_palabras) + ",incluyendo numeros")
    input("Presione una tecla para continuar...")


#################################################### Calculos ##########################################################

# Solicita valores, pasa a funcion calculo e imprime
def multiplicacion():
    multiplicando, multiplicador = solicitar_numeros()
    por_menos_uno = cambio_de_resultado(multiplicando, multiplicador)
    multiplicador = abs(multiplicador)
    multiplicando = abs(multiplicando)
    resultado = caculo_multiplicacion(multiplicando, multiplicador)
    if por_menos_uno:
        resultado = -resultado
    result = "La multiplicacion es " + str(resultado)
    print(result)
    input("Presione una tecla para continuar...")
    return resultado


# Realiza la multiplicacion por sumas sucesivas
def caculo_multiplicacion(multiplicando, multiplicador):
    suma = 0
    if multiplicando <= multiplicador:
        mayor = multiplicador
        menor = multiplicando
    else:
        mayor = multiplicando
        menor = multiplicador
    for numero in range(0, menor):
        suma += mayor
    return suma


# Solicita valores, pasa a funcion calculo e imprime.
def potencias():
    base, exponente = solicitar_numeros()
    resultado = calculo_potencias(base, exponente)
    print(resultado)
    input("Presione una tecla para continuar...")
    return resultado


# Relaiza calculo de potencias por multiplicacion sucesiva
def calculo_potencias(base, exponente):
    exponente_negativo = cambio_de_resultado(abs(base), exponente)
    multp = 1
    positivo = False
    if base != 0 and exponente != 0:
        if base < 0 and exponente % 2 == 0:
            positivo = True
        for i in range(0, abs(exponente)):
            multp *= base
        if exponente_negativo:
            multp = 1 / multp
            if positivo:
                multp = abs(multp)
    elif exponente == 0 and base != 0:
        multp = 1
    else:
        if base == exponente == 0:
            mensaje_error = "La base y el exponente no pueden ser 0 a la vez."
            return mensaje_error
        multp = 0
    resultado = "La potencia es " + str(multp)
    return resultado


# Realiza todos las divisiones por resta
def calculo_divison(dividendo, divisor):
    dividendo, divisor = abs(dividendo), abs(divisor)
    cociente = 0
    if dividendo < divisor:
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
    cociente, resto = calculo_divison(dividendo, divisor)
    if por_menos_uno:
        cociente = -cociente
    print("La division es {} y el resto {}.".format(cociente, resto))
    input("Presione una tecla para continuar...")


#####################################################Aux################################################################
def imprimir(parametro_1="", parametro_2=""):
    print(parametro_1, parametro_2)


# Pide valores , verifica que sean numeros y los devuelve
def solicitar_numeros():
    num1 = input("ingrese un numero: ")
    num2 = input("ingrese un numero: ")

    while not num1.lstrip("-").isdigit() and num2.lstrip("-").isdigit():
        input("No es un valor valido \nPresione una tecla para continuar...")
        num1 = input("ingrese un numero: ")
        num2 = input("ingrese un numero: ")
    num1 = int(num1)
    num2 = int(num2)
    return num1, num2


# Funcion para validar el cambio de signo en funciones de cálculo numerico, con variable booleana.
def cambio_de_resultado(num1="", num2=""):
    if num1 < 0 and num2 < 0:
        return False
    elif num1 < 0 or num2 < 0:
        return True


# Pide una cadena y la devuelve
def solicitar_texto():
    texto = ""
    while texto == "" or texto.strip().replace(" ", "").isalpha() == False:
        input("Ingrese un texto valido\nPresione una tecla para continuar...")
        texto = input("Ingrese texto: ")
    return texto