import random

sorteio = random.randint(1,30)
tentativas = 0

while tentativas < 3:
	tente = int(input('Teste sua sorte:'))
	tentativas = tentativas + 1

if tentativas == sorteio:
	print('Voce acertou') + str(tentativas) + 'vezes!'

else:
	print('Não foi desta vez...O numero sorteado foi: ' + str(sorteio))