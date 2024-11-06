'''
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.
'''
def numero_dias(numero):
    numero_dias = {
        1: "enero tiene 31",
        2: "febrero tiene 28",
        3: "marzo tiene 31",
        4: "abril tiene 30",
        5: "mayo tiene 31",
        6: "junio tiene 30",
        7: "julio tiene 31",
        8: "agosto tiene 31",
        9: "septiembre tiene 30",
        10: "octubre tiene 31",
        11: "noviembre tiene 30",
        12: "diciembre tiene 31",
        }
    return numero_dias.get(numero, "!ERROR¡")
numero = int(input("escriba el numero: "))
r = numero_dias(numero)
print(r)
