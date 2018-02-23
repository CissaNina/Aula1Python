import random

number = input('Digite seu numero: ')

sorteio = random.randint(1,30)


if number == sorteio:
	print('Voce acertou')

else:
	print('Não foi desta vez...')