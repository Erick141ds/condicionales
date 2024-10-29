'''
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
sin importar el número de alumnos. 
Realice un programa que permita determinar el pago a la compañía de autobuses 
y lo que debe pagar cada alumno por el viaje.
'''
a = int(input("escriba el total de alumnos: "))
total = 0
if a > 0:
    if a < 30: 
        total = 4000
    else: 
        if a <= 49: 
            total = a * 95
        else:
            if a <= 99:
                total = a * 70
            else:
                total = a * 65
print(f"el total a pagar por la renta del autobus es: ${total}")
print(f"el costo de el boleto es: ${total / a }")