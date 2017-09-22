import os
#opciones menu, devuelve int
def menu():
    opcion=0
    os.system('cls')
    while opcion==0:
        os.system('cls')
        try:      
            print("Selecciona una opción")
            print("1 - Numérico")
            print("2 - Cadenas de carácteres")
            print("3 - Salir")
            opcion=int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")         
    return opcion

#opciones menu num, devuelve int
def sub_menu_num():
    opcion=0
    os.system("cls")
    while opcion==0:
       os.system('cls')
       try:
           print("Selecciona una opción")
           print("1 - Multiplicación")
           print("2 - División y resto")
           print("3 - Potencia")
           print("4 - Volver al Menú principal")
           opcion=int(input("Ingrese una Opcion: "))
       except ValueError:
           print("Ingrese una opcion valida, solo un numero")
    return opcion

#opciones menu let, devuelve int
def sub_menu_let():
    os.system("cls")
    opcion=0
    while opcion==0:      
       try:
           print("Selecciona una opción")
           print("1 - Palabra mas Larga")
           print("2 - Palabra mas corta")
           print("3 - Contar Palabras")
           print("4 - Volver al Menú principal")
           opcion=int(input("Ingrese una Opcion: "))
       except ValueError:
           print("Ingrese una opcion valida, solo un numero")
    return opcion

def solicitar_cadena():
    cadena=""
    while cadena=="":
        try:  
            cadena=input("Ingrese una cadena de texto :")
        except ValueError:
            print("No ingreso una cadena..")
    return cadena
#solicitar_cadena()

# funcion pide opciones submenu

def opciones_submenu():
    opcion = 0
    while opcion == 0:
        try:
            print("1 - Continuar")
            print("2 - Ir al menú")
            print("3 - Ir al menú principal")
            opcion = int(input("¿Quiere continuar operando?: "))
        except ValueError:
            print("Ingrese una opcion valida, solo un numero")
    return opcion

# Se ingresan un String "frase".
'''La variable "listaLarga" devuelve un String de la o las palabras mas largas y "cantidadDeLetras" devuelve un String
de la cantidad de letras de la o las palabras.'''

def palabraMasLargaCantidadDeLetras(valor1):
    frase = valor1 #input("Ingrese una cadena de texto: ")
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

    mensaje = "Las palabras largas son {} y la cantidad de letras es {}.".format(listaLarga,cantidadDeLetras)
    return mensaje

# Devuelve un unico string para imprimir.

def string_corto(valor1):
    cadena = valor1 #input("Ingrese una cadena de texto: ")
    outside = "  "
    inside = ".,;"
    trans = cadena.maketrans(".,;!", "    ")
    cadena = cadena.translate(trans)
    lista_cadena = cadena.split()
    palabra_corta = lista_cadena[0]
    lista_auxiliar = []
    # lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
        if len(palabra_corta) > len(i):
            del lista_auxiliar[::]
            palabra_corta = i
            lista_auxiliar.append(palabra_corta)
        elif len(palabra_corta) == len(i):
            # lista_auxiliar.append(palabra_corta)
            lista_auxiliar.append(i)
            palabra_corta = i
    cantidad=len(palabra_corta)
    palabras_cortas = str(lista_auxiliar)
    palabras_cortas_mensaje="Las palabras cortas son {} y tienen {} caracteres ".format(palabras_cortas,cantidad)
    
    
    #print (palabras_cortas_mensaje)
    return palabras_cortas_mensaje  # palabras_cortas

# La acabo hacer y ver, parece andar bien

def contar_cadena(valor1):
    cadena = valor1 #input("Ingrese una cadena de texto: ")
    trans = cadena.maketrans(".,;!", "    ")
    cadena = cadena.translate(trans)
    lista_cadena = cadena.split()
    cantidad_palabras = len(lista_cadena)
    mensaje = "La cantidad de palabras en el texto es " + str(cantidad_palabras)

    return mensaje

# Imprime dentro de la funcion y aparte devuelve valores, habria que mandarlo en un mensaje.

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

# Se ingresan dos valores enteros "valorA" y "valorB".
# La variable "suma" devuelve un entero como resultado de la multiplicacion por suma sucesiva.

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


# Imprime dentro de la funcion y aparte devuelve valores, habria que mandarlo en un mesaje unicamente
# Y que imprima eso en la funcion generica imprimir.

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


# Solo con enteros, para cadenas habria que mod o hacer otra
# return un valor generico vacio y otro con cadena. No probe pero con un if se podria solucionar.

def solicitud():
    valor_1 = ""
    valor_2 = ""
    while valor_1 == "" and valor_2 == "":
        try:
            valor_1 = int(input("Ingrese un Parametro: "))
            valor_2 = int(input("Ingrese un Parametro: "))
        except ValueError:
            print("Ingrese un valor valido, solo un numero")
    return valor_1, valor_2


# Funcion imprimir generica

def imprimir(parametro_1="", parametro_2=""):
    print(parametro_1, parametro_2)
