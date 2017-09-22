

import funciones
import os
#Probar excepciones de funciones.
#Declaro variable de inicio 
salir=1
if salir==1:
    os.system('cls')
    continuar=3
    while continuar==3:
        #La func menu devuelve un int.
        opcion=funciones.menu()
        if opcion == 1:
            print("Estas en la Opcion Menú Numerico")
          
            #Declaro variable, que me va a permitir elegir si continuar dentro de las sub
            continuar=2
            while continuar==2:

                opcion=funciones.sub_menu_num()
                #Devuelve opcion del menu num

                if opcion == 1:
                    #Piso la anterior variable
                    continuar=1
                    #Opcion multiplicacion
                    #Ciclo que se podria modular en todas las opciones.
                    while continuar==1:
                        
                        #Pido valores genericos con msj genericos
                        valor1, valor2=funciones.solicitud()
                        parametro_1=funciones.multiplicacion(valor1, valor2)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo-controlo que sea casteable,se controla en la hoja funcion.
                        continuar=funciones.opciones_submenu()

                elif opcion == 2:
                    #Declaro la misma variable
                    #Piso la anterior variable
                    continuar=1
                    #Opcion division
                    
                    while continuar==1:
                        #Pido valores genericos con msj genericos
                        valor1, valor2=funciones.solicitud()
                        
                        try:
                            #Intento conseguir parametros
                            parametro_1, parametro_2=funciones.division(valor1,valor2)
                            funciones.imprimir(parametro_1,parametro_2) 
                            #continuar=funciones.opciones_submenu()
                            
                        except ValueError:
                           
                            mensaje=funciones.division(valor1, valor2) 
                            print(mensaje)
                            continuar=1
                        continuar=funciones.opciones_submenu()
                elif opcion == 3:
                    #Opcion de calculo de potencias
                    continuar=1
                    while continuar == 1:
                        valor1, valor2=funciones.solicitud()
                        try:
                            parametro_1=funciones.potencias(valor1, valor2)
                            funciones.imprimir(parametro_1)
                            #Sub menu ciclo
                            
                        except ValueError:
                             mensaje=funciones.potencias(valor1, valor2)
                             print(mensaje)
                             continuar=1
                        continuar=funciones.opciones_submenu()

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

                opcion=funciones.sub_menu_let()
                #Devuelve opcion del menu num

                if opcion == 1:
                    #Declaro la misma variable
                    #Opcion string largo
                    continuar=1
                    
                    while continuar==1:
                        valor1=funciones.solicitar_cadena()

                        parametro_1=funciones.palabraMasLargaCantidadDeLetras(valor1)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
           
                elif opcion == 2:
                    #Declaro la misma variable
                    continuar=1
                    #Opcion string corto
                    
                    while continuar==1:
                        valor1=funciones.solicitar_cadena()
                        parametro_1=funciones.string_corto(valor1)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()
                        
                elif opcion == 3:
                    continuar=1
                    
                    #Opcion contar palabras
                    while continuar==1:
                        valor1=funciones.solicitar_cadena()
                        parametro_1=funciones.contar_cadena(valor1)
                        funciones.imprimir(parametro_1)
                        #Sub menu ciclo
                        continuar=funciones.opciones_submenu()

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


