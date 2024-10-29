'''
para trabajar con condicionales
utiloizamos la instruccion if

if exp_bool:
    instrucciones
if exp_bool:
    instrucciones
else:
    instrucciones
if exp_bool:
    inst
elief exp_bool:
    inst
else:
    inst
'''
print('programa que lee 2 numeros')
print('nos dice cuel es el mayor')
num1 = int(input('ingresa un número: '))
num2 = int(input('ingrese otro numero: '))
if num1 > num2:
    print(f'el { num1 } es mayor')
else:
    print(f'el { num2 } es mayor')
