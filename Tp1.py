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
            for i in range(a , 0):
                suma += b
            suma = -suma
        else:
            for i in range(0, b):
                suma += a
    else:
        if abs(b) < a:
            for i in range(b , 0):
                suma += a
            suma = -suma
        else:
            for i in range(0, a):
                suma += b
    return suma

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

def division(a, b):
    div = 0
    cont = 0
    contadorDeDecimales = 0
    if a < 0 and b < 0 or a > 0 and b > 0:
            a = abs(a)
            b = abs(b)
            if a < b:
                if b % a == 0:
                    while b >= a:
                        b += -a
                        cont += 1
                    div = b
                    cont = 1/cont
                else:
                    while a < b:
                        a = a * 10
                        contadorDeDecimales += 1
                    while a >= b:
                        a += -b
                        cont += +1
                    div = a
                    cont = cont / (10 ** contadorDeDecimales)
            else:
                while a >= b:
                    a -= b
                    cont += 1
                div = a
    elif a < 0 or b < 0:
        a = abs(a)
        b = abs(b)
        if a < b and b % a == 0:
            while b >= a:
                b -= a
                cont += 1
            div = b
            cont = 1/-cont
        else:
            while a < b:
                a = a * 10
                contadorDeDecimales += 1
            while a >= b:
                a += -b
                cont += +1
            div = a
            cont = -cont / (10 ** contadorDeDecimales)
    return div, cont

def palabraMasLarga_cantidadDeLetras(c):
    palabraMasLarga = ""
    palabra = ""
    listalarga = []
    j = c.maketrans(",;.", "   ")
    c = c.translate(j).lower().split()
    palabraMasLarga = c[0]
    listalarga.append(palabraMasLarga)
    for palabra in c:
        if len(palabraMasLarga) < len(palabra):
            palabraMasLarga = palabra
            listalarga[0] = palabraMasLarga
        elif len(palabraMasLarga)==len(palabra) and palabraMasLarga!=palabra:
            listalarga.append(palabra)
    return listalarga






a = int(input("Ingrese un valor "))
b = int(input("Ingrese un valor "))
c = input("Ingrese un numero ")

print( palabraMasLarga_cantidadDeLetras(c))
print("hola mundo")