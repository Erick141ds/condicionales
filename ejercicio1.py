'''
preguntale al usuario su edad y muestre si es 
mayor de edad o no
entradas:
    edad: int
salidas:
    mesaje: str
'''
age = int(input(" ingresa tu edad: "))
if age >= 18:
    print('eres mayor de edad!')
else:
    print('eres menor de edad! ')
