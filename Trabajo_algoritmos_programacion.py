# Importo hoja de funciones
import funciones
import os

# Declaro variable de inicio
salir = 1
if salir == 1:
    os.system('cls')
    continuar = 3
    while continuar == 3:
        # La funcion menu devuelve un int.
        opcion = funciones.menu()
        if opcion == 1:
            print("Estas en la Opcion Menú Numerico")

            # Se Declara variable, que va a permitir elegir si continuar dentro de las sub
            continuar = 2
            while continuar == 2:
                # Se pide opciones al submenu, filtradas por excepcion

                opcion = funciones.sub_menu_num()
                # Devuelve opcion del menu num

                if opcion == 1:
                    # Se declara la anterior variable
                    continuar = 1
                    # Opcion multiplicacion
                    # Ciclo que se podria modular en todas las opciones.
                    while continuar == 1:
                        # Se pide valores genericos filtrados por excepcion.
                        valor1, valor2 = funciones.solicitud()
                        parametro_1 = funciones.multiplicacion(valor1, valor2)
                        funciones.imprimir(parametro_1)
                        # Sub menu ciclo, se controla que sea casteable
                        continuar = funciones.opciones_submenu()

                elif opcion == 2:
                    # Declaro la misma variable
                    # Cambia el valor de la variable para controlar los ciclos posteriores
                    continuar = 1
                    # Opcion division

                    while continuar == 1:
                        # Se Pide opciones al submenu, filtradas por excepcion
                        valor1, valor2 = funciones.solicitud()

                        try:
                            # Se Verifica caso de division
                            parametro_1, parametro_2 = funciones.division(valor1, valor2)
                            funciones.imprimir(parametro_1, parametro_2)
                            # continuar=funciones.opciones_submenu()

                        except ValueError:
                            # Si no se puede dividir
                            mensaje = funciones.division(valor1, valor2)
                            print(mensaje)
                            # seteo la variable y vuelvo a comenzar
                            continuar = 1
                        continuar = funciones.opciones_submenu()
                elif opcion == 3:
                    # Opcion de calculo de potencias
                    continuar = 1
                    while continuar == 1:
                        # Se Pide opciones a la funcion, filtradas por excepcion
                        valor1, valor2 = funciones.solicitud()
                        try:
                            parametro_1 = funciones.potencias(valor1, valor2)
                            funciones.imprimir(parametro_1)
                            # Sub menu ciclo

                        except ValueError:
                            # De no poder hacer la potencia
                            mensaje = funciones.potencias(valor1, valor2)
                            print(mensaje)
                            # Se setea variable para volver al ciclo
                            continuar = 1
                        continuar = funciones.opciones_submenu()

                elif opcion == 4:
                    # Opcion regreso al menu principal
                    continuar = 3

                else:
                    # Se setea variable para volver al ciclo
                    continuar = 2

                    print("Opcion Incorrecta")

        elif opcion == 2:

            print("Estas en la Opcion Menú de Cadenas de Texto")
            # Se Declara variable, que va a permitir elegir si continuar dentro de las sub
            continuar = 2
            while continuar == 2:

                opcion = funciones.sub_menu_let()
                # Devuelve opcion del menu num, filtrada por excepcion

                if opcion == 1:
                    # Se Declara la misma variable
                    # Opcion string largo
                    continuar = 1

                    while continuar == 1:
                        # Se piden parametros filtrados por excepcion
                        valor1 = funciones.solicitar_cadena()

                        parametro_1 = funciones.palabraMasLargaCantidadDeLetras(valor1)
                        funciones.imprimir(parametro_1)
                        # Sub menu ciclo
                        continuar = funciones.opciones_submenu()

                elif opcion == 2:
                    # Se Declara la misma variable
                    continuar = 1
                    # Opcion string corto

                    while continuar == 1:
                        valor1 = funciones.solicitar_cadena()
                        parametro_1 = funciones.string_corto(valor1)
                        funciones.imprimir(parametro_1)
                        # Sub menu ciclo
                        continuar = funciones.opciones_submenu()

                elif opcion == 3:
                    # Se setea variable de controla para el ciclo
                    continuar = 1

                    # Opcion contar palabras
                    while continuar == 1:
                        # Se pide variable filtrada por excepcion
                        valor1 = funciones.solicitar_cadena()
                        parametro_1 = funciones.contar_cadena(valor1)
                        funciones.imprimir(parametro_1)
                        # Sub menu ciclo
                        continuar = funciones.opciones_submenu()

                elif opcion == 4:
                    # Opcion menu principal
                    continuar = 3
                else:
                    print("Opcion Incorrecta")
                    # Se regresa al ciclo
                    continuar = 2
        elif opcion == 3:

            print("Saliendo")
            # Se cierra ciclo para salir del programa
            continuar = 0
            salir = 0
        else:
            print("Opcion Incorrecta")
            print("No llegué hasta acá")
else:
    # Salir del Programa
    salir = 0
