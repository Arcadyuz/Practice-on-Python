#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostar la suma de pares e impares desde 1 a 100
a=1
sumpar=0
sumimp=0
while a<=100:
    if a%2==0:
       sumpar=sumpar+a
       #print("La suma de numeros pares es: ",sumpar)
    else:
        sumimp=sumimp+a
        #print("La suma de numeros impares es: ",sumimp)
    a+=1
print("La suma de los pares es: ",sumpar)
print("La suma de los impares es: ",sumimp)