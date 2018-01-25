Idade=int(input('Quantos dias de vida?'))

ano = Idade / 365
mes = (Idade % 365) / 30
dias = (Idade % 365) % 30

print('%.0f anos(s)' % ano)
print ('%.0f mes(es)' % mes)
print ('%.0f' % dias)