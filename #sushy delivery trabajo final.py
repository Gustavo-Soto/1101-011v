#sushy delivery
import os
import time

limpieza_pantalla = "cls"
contador= 0
producto = 0
pika=0
otaku=0
pulpo=0
anguila=0
agregar = 1
boleta = 1
descuento = "soyotaku"
soyotaku = 0.10
total = contador

os.system(limpieza_pantalla)
while producto !=5:
    print("¡Bienvenido a sushi delivery!\n Lista de precios:")
    print(f"_"*31)
    print("1.-     pikachu rolls     $4500")
    print("2.-     Otaku rolls       $5000")
    print("3.-     Pulpo venenoso    $5200")
    print("4.-     Anguila electrica $4800")
    print("5.-     Salir")
    
    try:
        producto = int(input("Ingrese el numero de su producto deseado (1-5)"))
    except ValueError:
        print("Seleccion incorrecta, escoja nuevamente entre 1-5")
        time.sleep(2)
        os.system(limpieza_pantalla)
        continue

    if producto == 1:
            print("Pickachu roll añadido a carrito")
            agregar = input("¿desea agregar otro producto?\n1.-Si\2.-no)")
            if agregar == "1":
                  print("Agrega tu producto:")
                  contador= contador + 4500
                  pika = pika+1
            else:
                  print("Pasemos a la caja")                
            time.sleep(2)
            os.system(limpieza_pantalla)

    elif producto == 2:
            print("Otaku rolls añadido al carrito")
            agregar = input("¿desea agregar otro producto? (si/no)")
            if agregar == "si":
                  print("Agrega tu producto:")
                  contador = contador + 5000
                  otaku= otaku+1
            else:
                  print("Pasemos a la caja")
            time.sleep(2)
            os.system(limpieza_pantalla)

    elif producto ==3:
            print("Pulpo venenoso añadido al carrito")
            agregar = input("¿Desea agregar otro producto?(si/no)")
            if agregar == "si":
                print("Agrega tu producto:")
                contador = contador + 5200
                pulpo= pulpo +1
            else:
                  print("Pasemos a la caja")
            time.sleep(2)
            os.system(limpieza_pantalla)
            
    elif producto == 4:
            print("Anguila electrica añadida al carrito")
            agregar = input("¿Desea agregar otro producto?(si/no)")
            contador = contador + 4800
            anguila= anguila +1
            if agregar == "si":
                  print("Agrega tu producto:")
            else:
                  print("Pasemos a la caja")
            time.sleep(2)
            os.system(limpieza_pantalla)

    elif producto ==5:
          print("!Gracias por preferirnos¡")
          break
    else:
          print("Producto no es valido, elija una entre 1-5")
          time.sleep(2)
          os. system(limpieza_pantalla)

while boleta <=5:

      print(f"Su total es ${contador}")
      descuento=int(input("¿Tiene algun codigo de descuento?\n1.-Si\n2.-No)"))

      if descuento == "1":
            soyotaku=input("Escriba su codigo de descuento")
      elif soyotaku == "soyotaku":
            print("¡Usted tiene un 10% menos en su compra!")
            total= contador*soyotaku
            break
      else:
            print(f"Generando boleta{total}")

print(f"_"*31)
print("total productos")
print(f"_"*31)
print(" ")
print(f"pikachu rolls:          {pika}")
print(f"otaku rolls:            {otaku}")
print(f"pulpo:                  {pulpo}")
print(f"anguila elecrica:       {anguila}")
print(f"_"*31)
print(f"Subtotal:               {contador}")
print(f"Descuento por producto: {contador*soyotaku}")
print(f"Total:                  {total}")






