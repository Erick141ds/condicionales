'''
Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
sino se da un error.
entradas: 
Nombre
contraseña
salidas:
true
false
'''
n = input("usuario ")
c = input("clave ")
if n == "pepe" and c == "asdasd":
    print(f"has entrado al sistema: ")
else:
    print(f"!ERROR¡")