'''
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta
'''
jugador1 = input("jugador1 eliga sus opciones tijera, piedra, papel: ").lower()
jugador2 = input("jugador2 eliga sus opciones tijera, piedra, papel: ").lower()
def determinar_ganador(jugador1, jugador2):
   reglas = {
        1: "papel",
        2: "tijera",
        3: "piedra",
        }
if jugador1 not in reglas or jugador2 not in reglas:
    print("opcion incorrecta")
elif jugador1 == jugador2:
    print("empate")
elif reglas[jugador1] != jugador2:
    print("jugador1 gana")
else:
    print("jugador2 gana")
resultado = determinar_ganador(jugador1, jugador2)
print(resultado)