'''
Programador: Santiago Quintero 
Programa:Restaurante porcentaje
Fecha: 01/11/2022
'''

print("\n       Sistema de calculos del restaurante EL FAVORITO 🍲\n")

#Ingreso de valores 
totalConsumido = float(input("Ingresa el total consumido: "))
totalPersonas = int(input("Ingresa la cantidad de personas en la mesa: "))
print(f'\n      Opciones de propina\n')
print(f'1. 10% \n2. 15%\n3. Otros\n')
opcion = int(input("Seleccione una opcion: "))

#Operaciones del programa 
if opcion == 1:
    propina = totalConsumido * 0.1
if opcion == 2:
    propina = totalConsumido * 0.15
if opcion == 3:
    print(f'\n')
    aux = float(input("Ingresa la cantidad de propina: "))
    propina = aux
    
total = totalConsumido + propina
pagoXPersona = round(total / totalPersonas, 2) 

print(f'\nLa propina es de: 💵 $ {propina}')
print(f'Total consumido + propina: 💵 $ {total}')
print(f"La cantidad a pagar por cada persona es de: 💵 $ {pagoXPersona}\n")
print(f'            image.pngGracias por su preferencia\n')