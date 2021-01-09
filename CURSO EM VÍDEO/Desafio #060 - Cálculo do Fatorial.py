''' 
    Faça um programa que leia um número
qualquer e mostre o seu fatorial

Ex:
   5! = 5x4x3x2x1 = 120
   

1° Jeitinho simplificado

from math import factorial
numero = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, f))

'''
# 2° Jeitinho  melhorado

numero = int(input('Digite um número para calcular seu Fatorial: '))
calcular = numero
f = 1
print ('Calculando {}! = '.format(numero), end=' ')
while calcular > 0:
    print('{}'.format(calcular), end=' ')
    print(' x ' if calcular > 1 else '=', end=' ')
    f *= calcular
    calcular-= 1
print('{}'.format(f))
