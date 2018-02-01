login = input('Insira seu nome: ')
senha = input('Digite sua senha: ')
nasc = int(input('Qual seu ano de nascimento? '))
pet = input('Qual nome de seu pet? ')

quant_caracter = len(senha)

if quant_caracter < 6 or login == nasc or login == pet :
	print('Usuario errado ')

elif login and senha:
	print('não foi possível completar ')

elif login != senha:
	print('Usuario ok ')



