#ler distancia em metros e fazer conversões em outras medidas
met = float(input('Digite uma distancia em metros: '))
km = met / 1000
cm = met * 100
mm = met * 1000
print('O valor digitado em {} metros equivale a {} km , {} cm e {} mm'.format(met,km,cm,mm))
