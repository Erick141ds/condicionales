'''
Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
la edad es mayor o igual a dieciocho y el sexo es 'F'. 
En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''
n = int(input("escriba la nota: "))
e = int(input("escriba la edad: "))
s = input("escriba el sexo: ")
if n >= 5 and e >= 18 and s == 'f':
    print(f"!ACEPTADA¡")
elif n >= 5 and e >= 18 and s == 'm':
    print(f"¡POSIBLE!")
else:
    print("!NO ACEPTADA¡")