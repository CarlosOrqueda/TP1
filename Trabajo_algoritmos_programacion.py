'''Trabajo Práctico N°1
   Algoritmos y Programación
   Catedra: Guarna
   Integrantes: Carlos Orqueda
                Cristian Alarcón'''

# Importo hoja de funciones
import funciones
import os
#Menú
#Declaro variable de inicio

salir=False
while salir==False or continuar==2:
    
    opcion=funciones.menu()
    
    if opcion==1:
        continuar=1
        while continuar==1:
            opcion=funciones.sub_menu_num()
            if opcion==1:
                mensaje_1=str("un numero: ")
                mensaje_2=str("un numero: ")
                num_1, num_2=funciones.solicitud(mensaje_1, mensaje_2)
                producto=funciones.multiplicacion(num_1,num_2)
                funciones.imprimir(producto)
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==2:
                mensaje_1=str("un dividendo: ")
                mensaje_2=str("un divisor: ")
                dividendo, divisor=funciones.solicitud(mensaje_1, mensaje_2)
                try:                 
                    cociente=funciones.division(dividendo, divisor)
                    funciones.imprimir(cociente)
                except:
                    mensaje=funciones.division(dividendo,divisor)
                    print(mensaje)
                    continuar=funciones.opcion_submenu()
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==3:
                mensaje_1=str("una base: ")
                mensaje_2=str("un exponente: ")
                base,exponente=funciones.solicitud(mensaje_1, mensaje_2)
                try:  
                    potencia=funciones.potencia(base,exponente)
                    imprimir(potencia)
                except:
                    mensaje =funciones.potencias(base,exponente)
                    print(mensaje)
                    continuar=funciones.opcion_submenu()
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==4:
                #opcion=1
                continuar=0
                #salir=0
                #continuar=1
    elif opcion==2:
        continuar=1
        while continuar==1:
            opcion=funciones.sub_menu_let()
            if opcion==1:
                cadena=funciones.solicitar_cadena()
                cadena=funciones.armar_cadena(cadena)
                cadena=funciones.palabra_mas_larga(cadena)
                funciones.imprimir(cadena)
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==2:
                cadena=funciones.solicitar_cadena()
                cadena=funciones.armar_cadena(cadena)
                cadena=funciones.string_corto(cadena)
                funciones.imprimir(cadena)
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==3:
                cadena=funciones.solicitar_cadena()
                cadena=funciones.armar_cadena(cadena)
                cadena=funciones.contar_cadena(cadena)
                funciones.imprimir(cadena)
                #print("pido valores")
                continuar=funciones.opcion_submenu()
            elif opcion==4:
                continuar=0
                #salir=0
                            
        
    elif opcion==3:
        print("Saliendo")
        salir=True
        continuar=0
            
    else:
        print("No deberia llegar acá")
        
