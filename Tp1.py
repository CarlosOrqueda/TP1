# Se ingresan dos valores enteros "valorA" y "valorB".
# La variable "suma" devuelve un entero como resultado de la multiplicacion por suma sucesiva.

def multiplicacion(valorA, valorB):
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
    return suma


# Se ingresan dos valores enteros "valorA" y "valorB".
# La variable "multp" devuelve un entero o float como resultado de la potencia por multiplicacion.

def potencia(valorA, valorB):
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
            print(mensaje)
            return mensaje
        multp = 0
    mensaje = "La potencia es " + str(multp)
    return mensaje

a=5
b=5
mensaje = potencia(a,b)
print(mensaje)
# Se ingresan dos valores enteros "valorA" y "valorB".
'''La variable "resto" devuelve un entero y "cociente" devuelve un entero o float como resultado de la division por
resta sucesiva.'''

def division(valorA, valorB):
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
    return resto, cociente, mensaje


# Se ingresan un String "frase".
'''La variable "listaLarga" devuelve un String de la o las palabras mas largas y "cantidadDeLetras" devuelve un String
de la cantidad de letras de la o las palabras.'''


def palabraMasLargaCantidadDeLetras(frase):
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
    return listaLarga, cantidadDeLetras