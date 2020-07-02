# Ler algo na tela e responder qual o tipo primitivo e se é numérico ou é do alfabeto.
algo = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é: ',type(algo))
print('O que foi digitado, é numérico: ',algo.isnumeric(),'É do alfabeto: ',algo.isalpha())