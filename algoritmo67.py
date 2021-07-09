#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Diseñar un algoritmo que permita determinar si un número ingresado por teclado pueda mostrar su tabla de multiplicar desde 1 al 12.
a=int(input("ingrese el numero del cual desea ver su tabla de multiplicar: "))
i=1
for i in range(1, 13, 1):
    mult=a*i
    i+=1
    print("La tabla de multiplicar es: ",mult)