#Crie um programa que leia o nome de uma cidade e diga se comeca ou nao com 'Santo'.
cidade = str(input('Digite o nome de uma cidade: '.strip()))
cidade = cidade.upper()
print('Existe a paralvra Santo na frase digitada? ','SANTO'in cidade)
primeira = cidade.split()
print('A frase começa com a palavra Santo?','SANTO' in primeira[0])
