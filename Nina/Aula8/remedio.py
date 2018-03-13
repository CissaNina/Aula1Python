'''Maria precisa tomar remédio em 15 em 15 minutos.
Escreva um programa que mostre todos os horários em que Maria precisa tomar um remédio num período de um dia'''

for medicamento in range(0,24):
	for min in range(0,60,15):
	print(str(medicamento) + ':' + str(min))