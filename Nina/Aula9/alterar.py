'''Escreva um programa que receba uma palavra com mais de cinco
letras e troque as últimas quatro letras pela palavra gato'''


fruta = input('Digite uma palavra:')
contagem = len (fruta)

if contagem > 5:
	print ('Sua palavra:')
	letra = fruta[0:2]
	resultado = letra + str('gato')
	print (resultado)

else:
	print('Sua palavra nao tem o numero suficiente. ')

	
