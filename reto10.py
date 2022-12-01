'''
Programador: Santiago Quintero 
Programa:Reto 10 
Fecha: 30/ 11/2022
'''
'''
1) Lista que almacene el abecedario
2) Eliminar de la lista las letras que ocupen posiciones multiples de 3
3) Mostrar la lista resultante 
'''

listaABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

print(f"\n Abecedario: {listaABC}\n") # Lista con el abecedario

longitud = len(listaABC) # Longitud de la lista  
print(f" Cantidad de letras: {longitud}\n")

listaABC_Nueva = listaABC[::3]
print(f" Indice de tres en tres: {listaABC_Nueva}\n") # Imprimir la lista nueva

longitud2 = len(listaABC_Nueva) # Longitud de la lista  
print(f" Cantidad de letras: {longitud2}\n")
