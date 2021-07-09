##Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# De acuerdo a tres números , indicar cual es el menor y cual es el mayor.

Numero1=float(input("Ingrese un numero: "))
Numero2=float(input("Ingrese un numero: "))
Numero3=float(input("Ingrese un numero: "))
if Numero1 > Numero2 and Numero1 > Numero3:
    print("El primer numero es el mayor de todos ",Numero1)
if Numero2 > Numero3 and Numero2 > Numero1:
    print("El segundo numero es el mayor de todos ",Numero2)
if Numero3 > Numero1 and Numero3 > Numero2:
    print("El segundo numero es el mayor de todos ",Numero3),