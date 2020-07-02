# Ler um número e apresentar sua tabuada.
num1 = int(input('Digite o número para ver sua tabuada: '))

print('-'*12)
'''for i in range(1,11):
     print('{} x {} = {}'.format(num1,i,num1*i))
'''
i=0
while i<10:
    i+=1
    print('{:^1} x {:^2} = {:^2}'.format(num1,i,num1*i))

print('-'*12)