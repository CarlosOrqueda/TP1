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
    
    opcion=menu()
    
    if opcion==1:
        continuar=1
        while continuar==1:
            opcion=sub_menu_num()
            if opcion==1:
                mensaje_1=str("un numero")
                mensaje_2=str("un numero")
                num_1, num_2=solicitud(mensaje_1, mensaje_2)
                producto=multiplicacion(num_1,num_2)
                imprimir(producto)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==2:
                mensaje_1=str("un dividendo")
                mensaje_2=str("un divisor")
                dividendo, divisor=solicitud(mensaje_1, mensaje_2)
                try:                 
                    cociente=division(dividendo, divisor)
                    imprimir(cociente)
                except:
                    mensaje=division(dividendo,divisor)
                    print(mensaje)
                    continuar=opcion_submenu()
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==3:
                mensaje_1=str("una base")
                mensaje_2=str("un exponente")
                base,exponente=solicitud(mensaje_1, mensaje_2)
                try:  
                    potencia=potencia(base,exponente)
                    imprimir(potencia)
                except:
                    mensaje =potencias(base,exponente)
                    print(mensaje)
                    continuar=opcion_submenu()
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==4:
                #opcion=1
                continuar=0
                #salir=0
                #continuar=1
    elif opcion==2:
        continuar=1
        while continuar==1:
            opcion=sub_menu_let()
            if opcion==1:
                cadena=solicitar_cadena()
                cadena=palabraMasLargaCantidadDeLetras(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==2:
                cadena=solicitar_cadena()
                cadena=string_corto(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==3:
                cadena=solicitar_cadena()
                cadena=contar_cadena(cadena)
                imprimir(cadena)
                #print("pido valores")
                continuar=opcion_submenu()
            elif opcion==4:
                continuar=0
                #salir=0
                            
        
    elif opcion==3:
        print("Saliendo")
        salir=True
        continuar=0
            
    else:
        print("No deberia llegar acá")
        
