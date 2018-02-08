'''escreva um algorismo para recarga de celular, que receba o numero de telefone.
é comum perguntarmos novamente o numero para confirmar.
se o numero estiver errado peça para tentar novamente e exiba uma mensagem de erro, se não, mostre uma mensagem
informando que a a transação foi feita'''

celular =input('Qual seu numero? ')
confimacao = input('Digite o codigo enviado: ')

while confimacao != '1234':
	print('Tente novamente')
	confimacao = input('Digite o codigo enviado: ')

else:
	print('Transação foi feita... ')


