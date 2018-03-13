'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
number1=int(input('Digite um numero'))
number2=int(input('Digite um numero'))
number3=int(input('Digite um numero'))

decrescente = sorted((number1 ,number2,number3), key= int, reverse = True)

print ('Esse é a ordem' + str(decrescente))