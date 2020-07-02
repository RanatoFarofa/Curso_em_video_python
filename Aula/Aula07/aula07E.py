# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
num1 = int(input('Digite o número para ver sua tabuada: '))

'''for i in range(1,11):
     print('{}x{}={}'.format(num1,i,num1*i))
'''
i=1
while i<10:
    i+=1
    print('{}x{}={}'.format(num1,i,num1*1))