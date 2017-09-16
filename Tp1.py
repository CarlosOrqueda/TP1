# Se ingresan dos valores enteros como valor "a" y valor "b".
# La variable "suma" devuelve un entero como resultado de la multiplicacion por suma sucesiva.

def multiplicacion(a, b):
    suma = 0
    if a < 0 and b < 0 or a > 0 and b > 0:
        if a < 0 and b < 0:
            a = -a
            b = -b
        if a <= b:
            for i in range(0, a):
                suma += b
        elif a > b:
            for i in range(0, b):
                suma += a
    elif a < 0:

        if abs(a) < b:
            for i in range(a, 0):
                suma += b
            suma = -suma
        else:
            for i in range(0, b):
                suma += a
    else:
        if abs(b) < a:
            for i in range(b, 0):
                suma += a
            suma = -suma
        else:
            for i in range(0, a):
                suma += b
    return suma


# Se ingresan dos valores enteros como valor "a" y valor "b".
# La variable "multp" devuelve un entero o float como resultado de la potencia por multiplicacion.

def potencia(a, b):
    multp = 1
    if a != 0 and b != 0:
        if a > 0 and b > 0:
            for i in range(0, b):
                multp = multp * a
        elif b < 0:
            for i in range(b, 0):
                multp = multp * a
            multp = 1 / multp
        elif a < 0:
            for i in range(0, b):
                multp = multp * a
    else:
        multp = 0
    return multp


# Se ingresan dos valores enteros como valor "a" y valor "b".
'''La variable "resto" devuelve un entero y "cociente" devuelve un entero o float como resultado de la division por
resta sucesiva.'''

def division(a, b):
    resto = 0
    cociente = 0
    contadorDeDecimales = 0
    if a < 0 and b < 0 or a > 0 and b > 0:
        a = abs(a)
        b = abs(b)
        if a < b:
            if b % a == 0:
                while b >= a:
                    b += -a
                    cociente += 1
                resto = b
                cociente = 1 / cociente
            else:
                while a < b:
                    a = a * 10
                    contadorDeDecimales += 1
                while a >= b:
                    a += -b
                    cociente += +1
                resto = a
                cociente = cociente / (10 ** contadorDeDecimales)
        else:
            while a >= b:
                a -= b
                cociente += 1
            resto = a
    elif a < 0 or b < 0:
        a = abs(a)
        b = abs(b)
        if a < b and b % a == 0:
            while b >= a:
                b -= a
                cociente += 1
            resto = b
            cociente = 1 / -cociente
        else:
            while a < b:
                a = a * 10
                contadorDeDecimales += 1
            while a >= b:
                a += -b
                cociente += +1
            resto = a
            cociente = -cociente / (10 ** contadorDeDecimales)
    return resto, cociente


# Se ingresan una String "c".
'''La variable "listaLarga" devuelve un String de la o las palabras mas largas y "cantidadDeLetras" devuelve un String
de la cantidad de letras de la o las palabras'''


def palabraMasLargaCantidadDeLetras(c):
    cantidadDeLetras = 0
    listaLarga = []
    j = c.maketrans(",;.", "   ")
    c = c.translate(j).lower().split()
    palabraMasLarga = c[0]
    listaLarga.append(palabraMasLarga)
    for palabra in c:
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
