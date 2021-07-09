#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
#Mostrar si se aprueba la materia o no
nombre=input("Ingrese nombre del estudiante: ")
clases=int(input("Ingrese el total de numnero de clases del semestre: "))
ausencias=int(input("Ingrese el numero de fallas a clase: "))
notadefinitiva=float(input("Ingrese la nota definitiva del curso: "))
perdidaporfallas=clases*0.2
if ausencias>perdidaporfallas:
    print("Ud perdio por fallas y su nota es de 0")
else:
    print("felicidades aprobo el curso: ",notadefinitiva)