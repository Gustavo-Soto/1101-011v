#distribuidora de gas

import os
import time

limpieza_pantalla = "cls"
inicio = 1
menu = True
datos = 1
nombre = 0
telefono = 0
camion_est = 765000
contador = 0
cantidad_5 = 0
confirmar = 1
camion = 0
cilindro_5 = 0
cilindro_15 = 0
cilindro_45 = 0



while inicio:   
    while datos:       
        print("Bienvenido")
        print(f"_"*31)
        nombre=input("ingrese nombre cliente")
        telefono=input("Ingrese numero telefonicos")
        print(f"¡bienvenido {nombre}!")
        nombre = nombre

        correcto = input(f"¿Estos datos estan correctos? si(1) no (2)\n{nombre}\n{telefono}")

        if correcto == 1:
                print("Pasar a pedido")
                nombre = nombre
        else:
            print("ingrese datos correctamente")
            continue
        
        time.sleep(2)
        os.system(limpieza_pantalla)

        while menu:
                print("TIPOS DE CAMION")
                print(f"_"*40)
                print(f"1.-Camion estandar                 ${camion_est}")
                print("2.-Seleccionar carga especifica")
                print("3.-Imprimir boleta")

                if menu==1:
                    print("A seleccionado camion estandar")
                elif menu==2:

                    cilindro_5 = int(input("Indique cantidad de cilindros de 5kl:"))
                    cilindro_5 = cilindro_5

                    cilindro_15= int(input("Indique cantidad de cilindros de 15kl"))
                    cilindro_15 = cilindro_15

                    cilindro_45= int(input("Indique cantidad de cilindros de 45kl"))
                    cilindro_45 = cilindro_45

                    contador= cilindro_15 + cilindro_45 + cilindro_5

                elif menu == 3:
                     print("Imprimiendo boleta")



                      