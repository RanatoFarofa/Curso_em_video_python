# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
valor = float(input('Digite os metros para converter: '))
cent = valor*100
mili = valor*1000
print('O valor {} em métros corresponde a {} centimeros e {} milimetros'.format(valor,cent,mili))