#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Diseñar un algoritmo que permita calcular el factorial de un número, si el rango permitido debe estar entre 2 y 12
i=1
fact=1
numero=int(input("Ingrese un numero  "))
if numero >=2 and numero <=12:
	for i in range(numero):
		i+=1
		fact = fact*i
	print("El factorial de ",numero, "es: ",fact)  

else:
	print("Numero fuera de rango ")
