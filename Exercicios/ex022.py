#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas a letras maiusculas
#Quantas letras ao todo sem considerar os espaços 
#Quantas letras tem o primeiro nome 
nome = input('Digite seu nome completo: ')
print('O nome com todas as letras em maiúsculo: ',nome.upper())
print('O nome com todas a letras em minúsculo: ',nome.lower())
print('O nome possui {}, letras com espaços.'.format(len(nome)))
print('O nome possui {}, letras sem.'.format(nome.replace(' ','').__len__()))
separado = nome.split()
print('O seu primeiro nome é: ',separado[0])
print('O primeiro nome possui {}, letras'.format(len(separado[0])))
print('O primeiro nome possui {}, letras.'.format(len(nome.split()[0])))