'''
Realiza un programa que calcule la potencia, para ello pide por teclado 
la base y el exponente. Pueden ocurrir tres cosas:
El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
'''
b = int(input("escribe la base: "))
e = int(input("escribe el exponente: "))
if e > 0:
    print("la potencia es: ", b + e)
elif e == 0:
    print("la potencia es 1!")
else:
    print("la potencia es " , (1 / b * e))