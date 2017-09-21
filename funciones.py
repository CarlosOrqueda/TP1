
#se usa esta

def palabraMasLargaCantidadDeLetras():

    frase=cadena=input("Ingrese una cadena de texto: ")

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
    print ("Las palabras largas son: ",listaLarga)
    print ("Tienen ",cantidadDeLetras,"caracteres")
    return listaLarga, cantidadDeLetras
palabraMasLargaCantidadDeLetras()




#La acabo de ver, parece andar bien
def string_corto():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;!","    ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_corta= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_corta)>len(i):
          del lista_auxiliar[::]
          palabra_corta=i
          lista_auxiliar.append(palabra_corta)
       elif len (palabra_corta)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_corta=i
    
    print ("Las palabras cortas son: ",lista_auxiliar)
    palabras_cortas=lista_auxiliar
    return palabras_cortas


##Se usa esta
def division(valor1, valor2):
    valorA=int(valor1)
    valorB=int(valor2)

    
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
   
    print("La division es: ", cociente)
    print("El resto es: ", resto)
    return cociente, resto 

def multiplicacion(valor1, valor2):

    valorA=int(valor1)
    valorB=int(valor2)
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
    print("La multiplicacion es", suma)
    return suma

#multiplicacion(4,3)
###################

#string_corto()
#La acabo de ver, parece andar bien
def string_largo():
    
    cadena=input("Ingrese una cadena de texto: ")
    outside="  "
    inside=".,;"
    trans=cadena.maketrans(".,;","   ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    palabra_larga= lista_cadena[0]
    lista_auxiliar=[]
    #lista_auxiliar.append(palabra_corta)
    for i in lista_cadena:
       if len(palabra_larga)<len(i):
          del lista_auxiliar[::]
          palabra_larga=i
          lista_auxiliar.append(palabra_larga)
       elif len (palabra_larga)==len(i):
          #lista_auxiliar.append(palabra_corta)
          lista_auxiliar.append(i)
          palabra_larga=i
    
    print ("Las palabras largas son: ",lista_auxiliar)
    palabras_largas=lista_auxiliar
    return palabras_largas


#La acabo hacer y ver, parece andar bien
def contar_cadena():
    cadena=input("Ingrese una cadena de texto: ")
    trans=cadena.maketrans(".,;!","    ")
    cadena=cadena.translate(trans)
    lista_cadena=cadena.split()
    cantidad_palabras=len(lista_cadena)
    print("Hay",cantidad_palabras, "palabras en la cadena de texto.")
    
    return cantidad_palabras
#contar_cadena()

'''
#Ni la mire, pero parce ok.
def multiplicacion(valor1, valor2):
    a=int(valor1)
    b=int(valor2)
    c = 0
    suma=0
    if ((a < 0 and b < 0)):
        for i in range(b, 0):
            suma += - a
    elif (a > 0 and b < 0) or (a > 0 and b > 0):
        for i in range(0, a):
            suma += b
    else:
        if (b > 0 and a < 0):
            for i in range(0, b):
                suma += a
    print("La multiplicacion es", suma)

    return suma
'''
#se usa esta
def potencias(valor1, valor2):

    valorA=int(valor1)
    valorB=int(valor2)
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
    print("La potencia es", multp)   
    return multp
#potencias(4,2)


#No revise mucho
#La dejo de usar
'''
def potencias(valor1,valor2 ):
    c=int(valor1)
    d=int(valor2)
    multi = 1
    e = 0
    potencia = 0
    if (d >= 0):
        for i in range(0, d):
            multi = multi * c
        potencia = multi

    elif (d < 0):
        for i in range(d, 0):
            multi = multi * c
        potencia = 1 / multi
    print("La potencia es", potencia)
    return potencia
'''
#No revise si devuelve siempre
'''
def division(valor1, valor2):
    dividendo=int(valor1)
    sor=int(valor2)
    div = 0
    if ((abs(dividendo) > abs(sor)) and (sor != 0)):
        if ((dividendo > 0 and sor > 0) or (dividendo < 0 and sor < 0)):
            resto = dividendo

            while (abs(resto) >= abs(sor)):
                resto = resto - sor
                div =div + 1

        else:
            if ((dividendo > 0 and sor < 0) or (dividendo < 0 and sor > 0)):
                resto = abs(dividendo)
                sor = abs(sor)
                while (resto >= sor):
                    resto =resto - sor
                    div = div + 1
                div = -div
                resto = -resto

    else:
        if dividendo == 0:
            div = 0
            resto = dividendo
        elif sor == 0:
            print("No se puede dividir por 0")
    print("La división es:", div)
    print("El resto es:", resto)
    return div, resto
'''
######################
#La deje de usar
'''
def contar_palabras():
    cadena=input("Ingrese una cadena de texto: ")

    contador_palabras=0

    cadena=cadena.strip()
    for caracter in cadena:
        if caracter == " " or caracter == "." or caracter == ";" or caracter == ",":
            contador_palabras += 1
        else:
            contador_palabras = contador_palabras
    print("Hay ",contador_palabras, "palabras en la cadena de texto.")

    return contador_palabras
'''

    
#Solo la use en funciones con enteros, para cadenas no. Habia problemas con setear en el
#Hay que pasasrle un msj para cada funcion int.
#return un valor generico vacio y otro con cadena. No probe pero con un if se podria solucionar.
def solicitud():

    valor_1=input("Ingrese un Parametro: ")
    valor_2=input("Ingrese un Parametro: ")
    
    return valor_1,valor_2

def imprimir(parametro_1="", parametro_2=""):

    print(parametro_1, parametro_2)
