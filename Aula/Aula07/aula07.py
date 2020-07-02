# exemplo aula 06 - expresão aritimética
#testando precedencia 
# // - divide em partes iguais sem a ,
# % - divide e mostra somente o resto da divisão
#
print(5 + 3 * 2) #resultado == 11
print(3*5+4**2) # resultado 31
print(3*(5+4)**2) # resultado 243
print(25**(1/2)) # raiz quadrada de 25
print('='*20)# multiplica a string = por 20
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:-^20}!'.format(nome))
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
soma = n1+n2
divisao = n1/n2
subtracao = n1-n2
multiplicacao = n1*n2
potencia = n1**n2
divisaoigual = n1//n2
restodivisao = n1%n2
print('Os calculos dos valores são:\n')
print('Soma dos numeros {}'.format(soma)) 
print('Divisão dos numeros {}'.format(divisao))
print('Subtração dos numeros {}'.format(subtracao))
print('Multiplicação dos numeros {}'.format(multiplicacao)) 
print('Potenciação dos numeros {:.2f}'.format(potencia)) #{:.2f} - mostra apenas duas casas flutuantes.
print('Divisão em partes iguais {}'.format(divisaoigual))
print('Resto da Divisão {} '.format(restodivisao))
