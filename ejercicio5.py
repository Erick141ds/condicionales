'''
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario.
entradas:
    n1
    n2
salidas:
    true 
    false
'''
n1 = int(input("escriba el dividendo: "))
n2 = int(input("escriba el divisor: "))
if n2 == 0:
 print("!ERROR¡")
else:
    d = (n1 / n2 )
    print(f"el resultado es {d} ")