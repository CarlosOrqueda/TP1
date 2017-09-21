

import funciones
import os
#Las funciones de menu solo devuelven enteros, hay que revisar que lo que ingrese el usuario sea casteable.
#Habria que moverlas las funciones menu de aca a la otra hoja y hacer los llamados.
#Agregar una funcion que pida cadenas string generica, y verificar la impresion de funciones int
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

#Siempre comienza, igual el if inicial esta medio al dope pero abria que tabular todo y revisar.
#Probar excepciones de funciones.
#Resumiendo: Los menú funcionan(Basicamente) y los llamados tmb, funciones como string largo u corto, multiplicacion y potencia estan maso testeadas.
 
salir=1
if salir==1:
    os.system('cls')
    continuar=3
    while continuar==3:
        #La func menu devuelve un int.
        opcion=menu()
        if opcion == 1:
            print("Estas en la Opcion Menú Numerico")
          
            #Declaro variable, que me va a permitir eleigir si continuar dentro de las sub
            continuar=2
            while continuar==2:

                opcion=sub_menu_num()
                #Devuelve opcion del menu num

                if opcion == 1:
                    
                    continuar=1
                    #Opcion multiplicacion
                    #Ciclo que se podria modular en todas las opciones.
                    while continuar==1:

                        valor1, valor2=funciones.solicitud()
                        parametro_1=funciones.multiplicacion(valor1, valor2)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()                        #Hay que revisar que lo que ingrese el usuario sea casteable.
                        #O que lo vuelva a ingresar con aviso
           

                elif opcion == 2:
                    #Declaro la misma variable
                    continuar=1
                    #Opcion divisions
                    #Ciclo que se podria modular
                    while continuar==1:
                        valor1, valor2=funciones.solicitud()
                        
                        try:
                            parametro_1, parametro_2=funciones.division(valor1,valor2)
                            
                            funciones.imprimir(parametro_1,parametro_2)
                            #Sub menu ciclo
                            continuar=funciones.opciones_submenu()
                           
                            #Hay que revisar que lo que ingrese el usuario sea casteable.
                            #O que lo vuelva a ingresar con aviso
                        except ValueError:
                            mensaje=funciones.division(valor1, valor2)
                            print(mensaje)
                            continuar=1
                            
                elif opcion == 3:
                    #Opcion de calculo de potencias
                    continuar=1
                    #Ciclo que se podria modular
                    while continuar == 1:
       
                        valor1, valor2=funciones.solicitud()
                        parametro_1=funciones.potencias(valor1, valor2)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
                        #Hay que revisar que lo que ingrese el usuario sea casteable.
                        #O que lo vuelva a ingresar con aviso

                elif opcion == 4:
                    #Opcion regreso al menu principal
                    continuar=3

                else:
                    continuar=2
                    
                    print("Opcion Incorrecta")

        elif opcion==2:

            print("Estas en la Opcion Menú de Cadenas de Texto")
            #Declaro variable, que me va a permitir elegir si continuar dentro de las sub
            continuar=2
            while continuar==2:

                opcion=sub_menu_let()
                #Devuelve opcion del menu num
                #Hay que revisar que lo que ingrese el usuario sea casteable.
                #O que lo vuelva a ingresar con aviso

                if opcion == 1:
                    #Declaro la misma variable
                    #Opcion string largo
                    continuar=1
                    #Ciclo que se podria modular
                    while continuar==1:

                        parametro_1=funciones.palabraMasLargaCantidadDeLetras()
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
           
                elif opcion == 2:
                    #Declaro la misma variable
                    continuar=1
                    #Opcion string corto
                    #Ciclo que se podria modular
                    while continuar==1:
                        parametro_1=funciones.string_corto()
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
                        #Hay que revisar que lo que ingrese el usuario sea casteable.
                        #O que lo vuelva a ingresar con aviso

                elif opcion == 3:
                    continuar=1
                    #Ciclo que se podria modular
                    #Opcion contar palabras
                    while continuar==1:
                        parametro_1=funciones.contar_cadena()
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
                        #Hay que revisar que lo que ingrese el usuario sea casteable.
                        #O que lo vuelva a ingresar con aviso

                elif opcion == 4:
                    #Opcion menu principal
                    continuar=3
                else:
                    print("Opcion Incorrecta")
                    continuar=2
        elif opcion==3:

            print("Salir")
            continuar=0
            salir=0
        else:
            print("Opcion Incorrecta")
            print("No llegué hasta acá")
else:
    salir=0


