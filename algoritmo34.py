#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Determinar el precio de las llantas segun su cantidad se da un precio correspondiente
#si compran menos de 5 llantas 30kc/u, de 5 a 10 a 25kc/u y mas de 10 a 20kc/u
Cantidaddellantas = int(input("Ingrese la cantidad de llantas compradas: "))
if Cantidaddellantas < 5:
    Precio=30000*Cantidaddellantas
    print("Su valor a pagar es de: ",Precio)
if Cantidaddellantas >= 5 and Cantidaddellantas <= 10:
    Precio=25000*Cantidaddellantas
    print("Su valor a pagar es de: ",Precio)
if Cantidaddellantas >10:
    Precio=20000*Cantidaddellantas
    print("Su valor a pagar es de: ",Precio)