#calcular o valor do aluguel do veículo, sendo que a diaria custa 60 e o km 0,15.
dias_utilizados= int(input('Digite quantos dias você utilizou o veículo: '))
km_rodado = float(input('Digite quantos Km foram rodados com o veículo: '))
valor_diaria = dias_utilizados*60
valor_km = km_rodado*0.15
valor_final = valor_diaria + valor_km
print('Você utilizou o veículo por {} dias e rodou {}Km. O valor a pagar é de R${:.2f}.'.format(dias_utilizados,km_rodado,valor_final))