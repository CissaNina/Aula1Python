'''Crie uma programa que receba a idade de uma pessoa e verifique se ela pode votar
entrada: 21 dalianny
saída:dalianny tem 21 anos e pode votar'''

nome=input('Qual seu nome? ')
idade=int(input('Quantos anos você tem? '))

if idade > 18:
	print(nome  + ' tem' + str(idade) + ' anos e pode votar')
elif idade >15:
	print(nome  + ' tem' + str(idade) + ' é opcional')
else:
	print(nome + ' tem' + srt(idade) +' anos e ainda não chegou sua vez')

	



