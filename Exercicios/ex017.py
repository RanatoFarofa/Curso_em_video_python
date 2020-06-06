# Ler o valor do cateto oposto e adjacente de um triangulo retangulo e mostre o valor da hipotenusa.
import math
print('Vamos Caular a hipotenusa!')
cat_op = float(input('Digite o valor do cateto oposto do trinagulo retangulo :'))
cat_adj = float(input('Digite o valor do cateto adjacente do triangulo retangulo: '))
hipot = math.hypot(cat_adj,cat_op)
print('O cateto oposto é {} e o adjacente {}, fazendo as contas a hipotenusa é {:.2f}'.format(cat_op,cat_adj,hipot))