'''Crie um programa que receba a data de nascimento de uma pessoa, seu nome e verifique se ela pode votar'''
nome=input('Qual seu nome?')
nascimento=int(input('Em que ano você nasceu?'))

if nascimento < 2000:
	print('já pode votar') 

elif nascimento <=2002:
	print('Corre ainda da tempo')

else:
	print('Ainda não chegou seu tempo')