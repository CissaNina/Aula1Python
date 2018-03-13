'''Escreva um algoritimo que recebe uma data de nascimento de um usuario e compare essa data existente pré-cadastrada.
se a senha for diferente, exiba uma mensagem de erro e pergunte novamente a senha'''

usuario = input('Qual seu nome? ')
senha = input('Qual sua senha? ')

while senha != '29061994': 
	print('Erro tente novamente ')
	senha = input('Qual sua senha? ')

else:
	input('Senha certa!!! ')
