#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Diseñe un algoritmo que lea el nombre del estudiante, el valor de su matricula en un diplomado que responda si
# ¿ Es egresado de la universidad?, si la respuesta es SI, se le aplica un 25 % descuento. Muestre el nombre del estudiante y el valor de la matricula a pagar.

nombre=input("Ingrese el nombre del estudiante ")
pregunta=input("Es egresado de la universidad? ")
matricula=1500000
descuento=matricula*0.25
matriculadesc=matricula-descuento
respuesta= str("si")
if pregunta == respuesta:
    print("Bienvenido estudiante ",nombre, "su valor de matricula es de: ",matriculadesc)