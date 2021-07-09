#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar la tabla de multiplicar del numero ingresado por teclado
a=int(input("ingrese el numero del cual desea ver su tabla de multiplicar: "))
i=1
while i<=12:
    mult=a*i
    i+=1
    print("La tabla de multiplicar es: ",mult)