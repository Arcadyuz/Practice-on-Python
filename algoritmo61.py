#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Media de sumas de numeros pares e impares
n=1
sumpar=0
np=0
sumimp=0
npi=0
while n <= 10:
    numero=int(input("Ingrese 10 numeros "))
    if numero%2==0:
       sumpar+=numero
       np+=1
    else:
	    sumimp+=numero
	    npi+=1
    n+=1
sumpar=sumpar/np
sumimp=sumimp/npi
print("La media de los pares es: ",sumpar)
print("La media de los impares es: ",sumimp)