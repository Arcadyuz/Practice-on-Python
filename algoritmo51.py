#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar la suma de una serie que va desde 202 hasta 202 menos 2 la cantidad de veces que indique el numero ingresado por teclado
numero=int(input("ingrese el numero de terminos a completar "))
serie=202
suma=0
i=1
while i <= numero:
    serie-=2
    print(serie)
    suma+=serie
    i+=1
    
print("La suma total de la serie es: ",suma)
#print(x)a