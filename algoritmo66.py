#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Diseñar un algoritmo que permita determinar si un numero ingresado por teclado es primo o no

cont=0
numero=int(input("Ingrese un numero "))
for i in range(1, numero+1, 1):
	if numero%i == 0:
		cont+=1
if cont == 2: 
	print("El numero es primo ")
else:
	print("El numero no es primo ")	