'''
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
entradas:
cadena:
salidas:
mayusculas 
minusculas 
ambas
'''
c = input("cadena: ")
if c >= "A" and c <= "a": 
    print("la cadena esta en mayusculas!")
else:
    print("la cadena esta minusculas!")