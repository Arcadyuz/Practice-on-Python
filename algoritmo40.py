#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar el uso de if
edad=int(input("Ingrese la edad del paciente en meses: "))
nivel=float(input("Ingrese el nivel de hemoglobina en la sangre: "))
if edad > 0 and edad <= 1 and nivel < 13:
    print("EL paciente tiene anemia y es positivo ")
if edad > 1 and edad <= 6 and nivel < 10: 
    print("El paciente tiene anemia y es positivo ")
if edad > 6 and edad <= 12 and nivel < 11:
    print("El paciente tiene anemia y es positivo ")    
if edad > 12 and edad <= 60 and nivel < 11.5:
    print("El paciente tiene anemia y es positivo ")
if edad > 60 and edad <= 120 and nivel < 12.6:
    print("El paciente tiene anemia y es positivo ")
if edad > 120 and edad <= 180 and nivel < 13:
    print("El paciente tiene anemia y es positivo ")