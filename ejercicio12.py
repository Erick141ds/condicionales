'''
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
'''
t = int(input("escriba el tiempo de su llamada: "))
d = input("escriba el dia de lunes a domingo: ")
tn = input("escriba el turno del dia: ")
def calcular_cos_bas(t):
    if t <= 5:
        return t * 1.00
    elif t <= 8:
        return 5 * 1.00 + (t - 5) * 0.80
    elif t <= 10:
        return 5 * 1.00 + 3 * 0.80 +(t - 8 ) * 0.70
    else:
        return 5 * 1.00 + 3 * 0.80 + 2 * 0.70 +(t - 10)* 0.50
cos_bas = calcular_cos_bas(t)
if d == 'domingo':
    i = 0.3 
elif tn == 'mañana':
    i = 0.15
else: 
    i = 0.10 
costo_total = cos_bas * (1 + i)
print(f"costo de la llamada: {cos_bas:.2f} euros")
print(f"inpuesto: {i * 100: .0f}%")
print(f"costo de la llamada: {cos_bas:.2f} euros")
