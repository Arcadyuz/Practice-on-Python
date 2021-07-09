#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Se ha establecido un programa para estimular a los alumnos, el cual consiste en que si la nota promocional obtenido por los alumnos
#  durante todo el año en cada materia, se calculará las 6 notas finales de cada materia cursada. Si la nota promocional es mayor o 
# igual a 14 se le aplicará un descuento del 30% en la matricula del estudiante, 
# caso contrario se le aplicará un 10% adicional en el pago de su matricula.

nota1=float(input("Ingrese la nota 1 "))
nota2=float(input("Ingrese la nota 2 "))
nota3=float(input("Ingrese la nota 3 "))
nota4=float(input("Ingrese la nota 4 "))
nota5=float(input("Ingrese la nota 5 "))
nota6=float(input("Ingrese la nota 6 "))
Promedio=(nota1+nota2+nota3+nota4+nota5+nota6)/6
Matricula=float(input("Ingrese el valor de la matricula "))
if Promedio>=14:
    Descuento=Matricula*0.3
    Matriculadesc=Matricula-Descuento
    print("Felicitaciones obtuvo un descuento del 30porciento en su matricula ",Matriculadesc)
else:
    descuento=Matricula*0.1
    matriculadesc=Matricula-descuento
    print("Obtuvo un descuento del 10porciento en su matricula ",matriculadesc)

