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

valorA = -2
valorB = 3

resto, cociente= division(valorA, valorB)
print(resto,cociente)