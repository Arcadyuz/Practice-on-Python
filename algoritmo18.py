#Nombre: Alejandro Cadena
#Correo: Dobleaduo@gmail.com
# Diseñar un algoritmo que lea el nombre de un empleado, su salario básico por hora, el nro. de horas trabajadas en un mes. Nos pide lo siguiente:
#Calcular su salario mensual adicionalmente el subsidio de transporte, si su sueldo es mayor o igual a 2 salarios mínimos legal vigente. Tener en
# cuenta que el salario mínimo es 930 soles y el subsidio por transporte es 50 soles.
# Mostrar: el nombre del empleado, su salario mensual, el subsidio de transporte y su sueldo neto.


nombre =input("Ingrese el nombre del empleado: ")
salariomensual =float(input("Ingrese el salario mensual del empleado: "))
subsidio=50
sueldoneto = salariomensual+subsidio
if salariomensual>=1860:
    print("El nombre del empleado es ",nombre, "y su sueldo neto es de ",sueldoneto)