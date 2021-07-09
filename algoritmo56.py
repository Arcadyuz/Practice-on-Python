#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Reloj por teclado
hr = 0
min= 0
seg = 0
import time
hr=int(input("Ingrese la Hora "))
min=int(input("Ingrese los Minutos "))
seg= int(input("Ingrese los Segundos "))
while hr < 24:
	while min < 60:
		while seg < 60:
			print("",hr,":",min,":",seg)
			seg+=1
			time.sleep(1)
	min+=1;
	seg=0;
hr+=1;
min=0;
#seg=0