#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Muestra de resto y cociente mediante restas
resto = 0
co = 0
num=int(input("Ingrese el numerador "))
den=int(input("Ingrese el denominador "))
while num > den:
	num = num-den
	resto = num
	co+=1
print("El residuo es: ",resto)
print("El cociente es: ",co)