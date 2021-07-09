#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Factorial de numeros ingresados por teclado
numero=int(input("Ingrese un numero  "))
i=1
fact=1
#if numero > 0:
    #print("El numero esta dentro del rango permitido ")
while i < numero:
	i+=1
	fact = fact*i    
print("El factorial de ",numero, "es: ",fact)    
#else:
#    print("El numero no esta dentro del rango permitido")
