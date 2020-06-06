#Leia quanto dinheiro na quarteira a pessoa tem e mostre quantos dólares ela pode comprar. Considerando dolar 3,27.
wallet = float(input('Digite o valor que possui na carteira: '))
dolar = (wallet / 3.27)
print('Sua carteira possui {:.2f} reais se convertido em dólar, vale {:.2f} dólares'.format(wallet,dolar))
