n1=int(input('Digite um numero:'))
n2=int(input('Agora outro: '))
n3=int(input('Só mais um: '))

if n1 > n2 and n1 > n3:
        print (str(n1) + 'é o maior numero!! ')

elif n2 > n1 and n2 > n3:
	print(str(n2) + 'é o maior ')

else:
	print(str(n3) + 'é o maior ')
