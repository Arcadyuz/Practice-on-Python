#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000, y en ese caso diseña un algoritmo para saber cuanto dinero tendrá finalmente en su cuenta.

inversion=float(input("Ingrese la cantidad de dinero a invertir: "))
tasainteres=float(input("Ingrese la tasa de interes a manejar (0-100): "))
Intereses=(inversion*tasainteres)/100
capitalfinal=inversion+Intereses
if Intereses>7000:
    print("Su capital total es de: ",capitalfinal)
else:
    print("Puede volver a invertir sus intereses")