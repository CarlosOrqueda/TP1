def division(valorA, valorB):
    resto = 0
    cociente = 0
    contadorDeDecimales = 0
    porMenosUno = 0

    if valorA < 0 or valorB < 0:
        porMenosUno = -1
    valorA = abs(valorA)
    valorB = abs(valorB)
    if valorA < valorB and valorB % valorA == 0:
        while valorB >= valorA:
            valorB += -valorA
            cociente += 1
        resto = valorB
        if porMenosUno == -1:
            cociente = -cociente
        cociente = 1 / cociente
    else:
        while valorA < valorB:
            valorA = valorA * 10
            contadorDeDecimales += 1
        while valorA >= valorB:
            valorA -= valorB
            cociente += 1
        resto = valorA
        if porMenosUno == -1:
            cociente = -cociente
        cociente = cociente / (10 ** contadorDeDecimales)

    return resto, cociente



valorA = 2
valorB = 12

resto, cociente= division(valorA, valorB)
print(resto,cociente)