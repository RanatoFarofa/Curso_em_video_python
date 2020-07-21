# Faça um programa que leia o numero de 0 a 9999 e mostre na tela cada um dos digitos separados
'''num = input('Digite um numero inteiro de 0 9999 : ')
print('O número digitado é {}. '.format(num))
separado = num.split()
unidade = separado[0][-1]
dezena = separado[0][-2]
centena = separado[0][-3]
milhar = separado[0][-4]
print('Separação do numero: ',separado)
print('Unidade: ',unidade)
print('Dezena: ',dezena)
print('Centena: ',centena)
print('Milhar: ',milhar)'''
#Solução
num = int(input('Digite um numeor inteiro de 0 até 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('O número digitado é {} , que contém a unidade {} , a dezena {}, a centena {}  e o milhar {} '.format(num,unidade,dezena,centena,milhar))