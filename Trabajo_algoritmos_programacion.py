'''Trabajo Práctico N°1
   Algoritmos y Programación
   Catedra: Guarna
   Integrantes: Carlos Orqueda
                Cristian Alarcón'''

# Importo hoja de funciones
import funciones
import os

# Menú
# Declaro variable de inicio
salir = False
while salir == False or menu == 2:
    # si menu=2-vuelve al menú principal
    # si menu=1-vuelve al menu de letras o numerico segun corresponda
    opcion = funciones.menu()
    if opcion == 1:
        menu = 1
        while menu == 1:
            # Entra al menu numerico
            opcion = funciones.sub_menu_num()
            # Selecciona opcion del menu numerico
            if opcion == 1:
                #Solicita valores a calcular con msj por función.
                mensaje_1 = str("Ingrese un numero: ")
                mensaje_2 = str("Ingrese un numero: ")
                num_1, num_2 = funciones.solicitud(mensaje_1, mensaje_2)
                producto = funciones.multiplicacion(num_1, num_2)
                funciones.imprimir(producto)
                #Pide nuevamente la opcion continuar
                menu = funciones.opcion_submenu()
            elif opcion == 2:
                #Solicita valores a calcular con msj por función.
                mensaje_1 = str("Ingrese un dividendo: ")
                mensaje_2 = str("Ingrese un divisor (No se puede dividir por cero): ")
                dividendo, divisor = funciones.solicitud(mensaje_1, mensaje_2)
                try:
                    cociente = funciones.division(dividendo, divisor)
                    funciones.imprimir(cociente)
                except:
                    mensaje = funciones.division(dividendo, divisor)
                    print(mensaje)
                    menu = funciones.opcion_submenu()
                #Pide nuevamente la opcion continuar
                menu = funciones.opcion_submenu()
            elif opcion == 3:
                #Solicita valores a calcular con msj por función.
                mensaje_1 = str("Ingrese una base: ")
                mensaje_2 = str("Ingrese un exponente: ")
                base, exponente = funciones.solicitud(mensaje_1, mensaje_2)
                try:
                    potencia = funciones.potencia(base, exponente)
                    funciones.imprimir(potencia)
                except:
                    mensaje = funciones.potencia(base, exponente)
                    print(mensaje)
                #Pide nuevamente la opcion continuar
                menu = funciones.opcion_submenu()
            elif opcion == 4:
                menu = 0
                # salir=0
                # continuar=1
    elif opcion == 2:

        menu = 1
        while menu == 1:
            # Entra al menu de cadenas de texto
            opcion = funciones.sub_menu_let()
            # Selecciona accion
            if opcion == 1:
                cadena = funciones.solicitar_cadena()
                cadena = funciones.armar_cadena(cadena)
                cadena = funciones.palabra_mas_larga(cadena)
                funciones.imprimir(cadena)
                menu = funciones.opcion_submenu()
            elif opcion == 2:
                cadena = funciones.solicitar_cadena()
                cadena = funciones.armar_cadena(cadena)
                cadena = funciones.string_corto(cadena)
                funciones.imprimir(cadena)
                menu = funciones.opcion_submenu()
            elif opcion == 3:
                cadena = funciones.solicitar_cadena()
                cadena = funciones.armar_cadena(cadena)
                cadena = funciones.contar_cadena(cadena)
                funciones.imprimir(cadena)
                menu = funciones.opcion_submenu()
            elif opcion == 4:
                menu = 0
                # salir=0

    elif opcion == 3:
        # Sale del programa
        print("Saliendo...")
        input("Presione una tecla para continuar...")
        salir = True
        menu = 0

    else:
        print("No deberia llegar nunca acá(Las alternativas estan controladas en las excepciones del menú)")
