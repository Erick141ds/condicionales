'''
Escribe un programa que lea un número e indique si es par o impar.
entradas:
n1
salidas 
par:
inpar:
'''
n1 = int(input("escriba un numero: "))
r = n1%2
if r == 0:
    print(f"el {n1} es par!")
else: 
    print(f"el {n1} es inpar!")