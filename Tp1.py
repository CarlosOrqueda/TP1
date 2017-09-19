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
        multp = 0
    return multp


# Se ingresan dos valores enteros "valorA" y "valorB".
'''La variable "resto" devuelve un entero y "cociente" devuelve un entero o float como resultado de la division por
resta sucesiva.'''

def division(valorA, valorB):
    resto = 0
    cociente = 0
    contadorDeDecimales = 0
    if valorA < 0 and valorB < 0 or valorA > 0 and valorB > 0:
        valorA = abs(valorA)
        valorB = abs(valorB)
        if valorA < valorB:
            if valorB % valorA == 0:
                while valorB >= valorA:
                    valorB += -valorA
                    cociente += 1
                resto = valorB
                cociente = 1 / cociente
            else:
                while valorA < valorB:
                    valorA = valorA * 10
                    contadorDeDecimales += 1
                while valorA >= valorB:
                    valorA -= valorB
                    cociente += 1
                resto = valorA
                cociente = cociente / (10 ** contadorDeDecimales)
        else:
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
    elif valorA < 0 or valorB < 0:
        valorA = abs(valorA)
        valorB = abs(valorB)
        if valorA < valorB and valorB % valorA == 0:
            while valorB >= valorA:
                valorB -= valorA
                cociente += 1
            resto = valorB
            cociente = 1 / -cociente
        else:
            while valorA < valorB:
                valorA = valorA * 10
                contadorDeDecimales += 1
            while valorA >= valorB:
                valorA -= valorB
                cociente += 1
            resto = valorA
            cociente = -cociente / (10 ** contadorDeDecimales)
    return resto, cociente


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