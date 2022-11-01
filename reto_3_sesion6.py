'''
Programador: Santiago Quintero 
Programa:Mostrar número si es par o iimpar
Fecha: 01/11/2022
'''
print('\n                         Número par o impar\n')

numero = int(input("\n Ingrese un número: "))

resultado = numero % 2

if resultado == 0:
    print(f'\nEl número {numero} es par\n')
else:
    print(f'\nEl número {numero} es impar\n')