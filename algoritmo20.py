#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Diseñar un algoritmo que muestre si una persona tiene ingresos o no, pero para ser mas específicos se responderá a las siguientes preguntas:
#Si no tiene efectivo entonces esta en nros rojos.
#Si tiene poco efectivo menor a 1000, que muestre que debe trabajar mas.
#Si tiene un efectivo menor a 2000 entonces significa que le va regularmente bien.
#Si tiene un efectivo mayor a 2000 entonces significa que tiene buen status financiero.

nombre=input("Ingrese su nombre: ")
ingresos=float(input("De el total de sus ingresos: "))
if ingresos<=0:
    print("Ud esta en numeros rojos")
if ingresos> 0 and ingresos<1000:
    print("Ud tiene que trabajar más")
if ingresos>1000 and ingresos<2000:
    print("Vamos bien")
if ingresos>2000:
    print("Ud tiene buen status financiero")