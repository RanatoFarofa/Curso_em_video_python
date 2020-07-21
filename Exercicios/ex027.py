#Fazer um programa que leia um nome completo e mostre somente o primeiro e o ultimo nome.
nome =  input('Digite seu nome completo: ').strip()
dividido = nome.split()
print('O primeiro e ultimo nome é:',dividido[0],dividido[-1])