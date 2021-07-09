#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar cuantos empleados de una empresan ganan salarios entre 100 y 300 y cuantos ganan mas de eso e informar a la empresa el gasto en salarios del personal
n=int(input("Ingrese la cantidad de empleados "))

empleado=0
Empleado=0
sueldo=0
a=1
while a <= n:
	sueldo=int(input("Ingrese el sueldo del empleado "))	
	if sueldo >=100 and sueldo<=300:
		empleado+=1
		a+=1
	elif sueldo>300:
		Empleado+=1
		a+=1
	else:
		print("Error")
print("El numero de empleados con sueldo entre 100 y 300 es: ",empleado)
print("El numero de empleados con sueldo mayor de 300 es: ",Empleado)