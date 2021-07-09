#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar la media de los numeros ingresados por teclado
numero=float(input("Ingrese un numero "))
media = 0
cantidad = 0
#lt= media / cantidad
while numero > 0:
    media = media + numero
    cantidad = cantidad + 1
    numero = float(input("Ingrese otro numero: "))
lt= media / cantidad
print("La media es de: ",lt)