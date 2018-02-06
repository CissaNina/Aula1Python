'''Faça um programa que pergunte o preço de três produtos 
e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.'''
prod1=int(input('Qual produto?'))
prod2=int(input('Qual produto?'))
prod3=int(input('Qual produto?'))

melhorvalor=min (prod1, prod2,prod3)

print('Esse é mais enconta' + '%.2f' % float(melhorvalor))

