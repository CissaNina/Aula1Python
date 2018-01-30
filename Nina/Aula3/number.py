'''Escreva um programa que imprima todos os números pares entre 1 e 100, incluindo eles se for o caso.'''
X = int(input())

if X < 0:
	print('numero negativo')

elif X % 2 == 0:
	print('numero positivo par')

else:
	print('numero positivo impar')

