'''
Realiza un programa que pida el dia de la semana (del 1 al 7) y escriba 
el dia correspondiente. 
Si introducimos otro número nos da un error
entradas 
dias de la semana 
salidas 
error 
'''
def dia_s(dia):
    dia_s = {
    1 : "Lunes",
    2 : "Martes",
    3 : "Mircoles",
    4 : "Jueves",
    5 : "Viernes",
    6 : "Savado",
    7 : "Domingo",
    }
    return dia_s.get(dia,"!ERROR¡ el numero que  dijito no es correcto")
dia = int(input("escriba el dijito de la semana: "))
r = dia_s(dia)
print(r)
