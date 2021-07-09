#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#mostrar el numero mayor y menor de 5 numeros ingresados por teclado
i=1
nummayor=0
nummenor=0
#numeros=int(input("Ingrese los 5 numeros mediante teclado: "))
while i<=5:
    numero=int(input("ingrese un numero "))
    
    if i==1:
        nummayor=numero
        
        nummenor=numero

    if numero>nummayor:

        nummayor=numero

    if numero<nummenor:

        nummenor=numero
    i+=1

print("Numero mayor es: ",nummayor, "Y el numero menor es: ",nummenor)