'''
Programa que pida tres números y los muestre ordenados (de mayor a menor);
entrada:
n1
n2
n3
salidas
ordenar:
'''
n1 = int(input("escriba el valor 1: "))
n2 = int(input("escriba el valor 2: "))
n3 = int(input("escriba el valor 3: "))
if n1 > n2:
    if n2 > n3:
        print(f"el orden de los numeros es {n3, n2, n1}")
    elif n1 > n3:
        print(f"el orden de los numeros es {n2, n3, n1}")
    else:
        print(f"el orden de lols nemeros es {n2, n1, n3}")
else:
    if n1 > n3:
        print(f"el orden de los numeros es {n3, n1, n2}")
    elif n2 > n3:
        print(f"el orden de los numeros es {n1, n3, n2}")
    else:
        print(f"el orden de los numeros es {n1, n2, n3}")