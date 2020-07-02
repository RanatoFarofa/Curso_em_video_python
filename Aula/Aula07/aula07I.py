# Ler o salário do funcionário e mostrar com acrecimo de 15% 
salario = float(input('Digite o valor do seu salário: '))
aumento = salario + (salario*(15/100))
print('O seu salário de {} obteve um aumento de 15% e foi para {} , parabáns!'.format(salario,aumento))