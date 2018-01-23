name=input('Qual seu nome? ')
preço=int(input('valor '))
quantidade=int(input('quantidade '))
total= preço * quantidade
print('money ' + str(name) + ' ' + str(preço) + ' ' +str(quantidade) + ' R$' + str('%.2f' % total))