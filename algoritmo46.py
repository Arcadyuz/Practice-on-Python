#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#mostrar la suma de una serie desde 2 hasta el numero ingresado por teclado saltando de 2 en 2
numero=int(input("ingrese el ultimo numero de la serie "))
suma=0
serie=2
while serie <= numero:
    print(serie)
    suma=suma+serie
    serie=serie+2
print("La suma total de la suma es: ",suma)