#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Muestro de cantidad de numeros dentro de rangos especificos
num=int(input("ingrese un numero "))
n=0
a=0
b=0
c=0
while n < num:
	if n < 15:
		a+=1
	elif n >= 25 and n <= 45:
		b+=1
	elif n > 50:
		c+=1
	n+=1
print("Son menores que 15: ",a)
print("Estan entre 25 y 45: ",b)
print("Son mayores a 50: ",c)