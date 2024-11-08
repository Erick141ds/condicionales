'''
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta
'''
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "empate" 
    elif (opcion1 == "piedra " and opcion2 == "tijera") or \
         (opcion1 == "tijera" and opcion2 == "papel") or \
         (opcion1 == "papel" and opcion2 == "piedra"):
        return "gana jugador 1"
    else:
        return "gana jugador 2"

jugador1 = input("jugador 1 eliga tijera, piedra o papel: ").lower()

jugador2 = input("jugador 2 eliga tijera, piedra o papel: ").lower()
    
reglas = ["papel", "tijera", "piedra"]

if jugador1 not in reglas or jugador2 not in reglas:
    print("opcion incorrecta")
else:
    resultado = determinar_ganador(jugador1, jugador2)
    print(resultado)