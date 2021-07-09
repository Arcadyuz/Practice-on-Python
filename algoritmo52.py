#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el factorial de un numero entre 1 y 15 y tambien mostrar un mensaje si el numero esta fuera de rango
numero=int(input("Ingrese un numero entre el 1 al 15 "))
i=1
fact=1
if numero > 0 and numero <=15:
    print("El numero esta dentro del rango permitido ")
    while i<numero:
        i+=1
        fact=fact*i    
    print("El factorial de ",numero, "es: ",fact)    
else:
    print("El numero no esta dentro del rango permitido")
