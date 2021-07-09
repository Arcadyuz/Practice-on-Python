#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar la cantidad de numeros multiplos de 3 desde 1 hasta el numero ingresado por teclado
num=int(input("Ingrese un numero: "))
i=3
cant=0
while i<=num:
    if i%3==0:
        print(i)
        cant+=1
    i+=1
print("La cantidad de multiplos de 3 es: ",cant)