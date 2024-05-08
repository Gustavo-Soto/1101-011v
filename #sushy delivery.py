#sushy delivery
import os
import time

limpiez_pantalla = "cls"
contador= 0
producto = 0

os.system(limpiez_pantalla)
while producto !=5:
    print("!Bienvenido a sushi delivery¡\n Lista de precios:")
    print("1.-     pikachu rolls     $4500")
    print("2.-     Otaku rolls       $5000")
    print("3.-     Pulpo venenoso    $5200")
    print("4.-     Anguila electrica $4800")
    print("5.-     Salir")
    print(" ")
    
    try:
        producto = int(input("Ingrese el numero de su producto deseado (1-4)"))
    except ValueError:
        print("Seleccion incorrecta, escoja nuevamente entre 1-5")
        continue

    if producto == 1:
            print("Pickachu roll añadido a carrito")
            contador= contador + 4500
    elif producto == 2:
            print("Otaku rolls añadido al carrito")
            contador = contador + 5000
    elif producto ==3:
          print("Pulpo venenoso añadido al carrito")
          contador = contador + 5200
    elif producto == 4:
          print("Anguila electrica añadida al carrito")
    elif producto ==5:
          print("!Gracias por visitarnos¡")
          break
    else:
          print("Producto no es valido, elija una entre 1-5")
          time.sleep(2)
          os. system(limpiez_pantalla)



    

    