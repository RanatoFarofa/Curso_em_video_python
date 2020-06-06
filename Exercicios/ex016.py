# Crie um programa que leia um numero real e mostre sua porção inteira.
from math import trunc

n = float(input('Digite um nuemro real :'))
print('O numero digitado {} a sua porção inteira é {} '.format(n,trunc(n)))
