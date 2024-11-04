'''
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".
'''
def caras_dado(caras):
    caras_dado ={
    1: "6",
    2: "5",
    3: "4",
    4: "3",
    5: "2",
    6: "1",
    }
    return caras_dado.get(caras,"!ERROR¡ : numero incorrecto")
caras = int(input("escriba las caras del dado: "))
r =  caras_dado(caras)
print(r)