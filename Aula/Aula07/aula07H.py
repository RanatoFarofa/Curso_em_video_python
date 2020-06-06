#Leia o preço do produto e aplique 5% de desconto e apresente o novo preço 
produt = float(input('Digite o valor do produto: '))
desc = produt - (produt *(5/100))
print('O produto de {} com desconto de 5% , sai por {} '.format(produt,desc))