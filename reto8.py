'''
Programador: Santiago Quintero 
Programa:Reto 8 
Fecha: 14/ 11/2022
'''
print("\n                 Reto sesion 8   \n")
nombre = input("\nIngresa tu nombre completo: ")
print()
print(f"Nombre ingresado en ayuscula: {nombre.upper()}\n")
print(f"Nombre ingresado en minusculas: {nombre.lower}\n")
print(f"Primera letar del nombre(s) y apellido(s) en mayuscula: {nombre.title()}\n")
print(f"El nombre ingresado tiene {len(nombre)} caracteres, contando los espacios\n")
nombre = nombre.replace(" ", "")
print(f"El nombre ingresado  tiene {len(nombre)} letras\n")