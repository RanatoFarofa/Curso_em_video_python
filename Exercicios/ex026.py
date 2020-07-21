#Crie um programa que leia uma frase qualquer e mostre Quantas vezes aparece a letra 'A'.
# Em que posição aparece a primera vez, em qual posiçao aparece pela ultma vez.
frase = input('Digite uma frase qualquer: ').upper().strip()
print('Sua frase tem {}, posições'.format(frase.__len__()))
print('Sua frase possui {}, letras a'.format(frase.count('A')))
print('A primeira vez que a letra a aparece é na posição: ',frase.find('A')+1)
#ultimo = frase[-10:]
print('A ultima vez que a letra a aparece é na posição: ',frase.rfind('A')+1) #rfind começa a pesquisa pelo lado direito.