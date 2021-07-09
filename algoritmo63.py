#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Sume de numeros pares entre 1 y 200
suma=0
for numero in range(1,201):
	if numero%2==0:
		suma=suma+numero
print("La suma de los numeros pares es: ",suma)