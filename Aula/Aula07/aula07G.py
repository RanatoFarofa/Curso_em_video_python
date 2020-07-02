#Ler altura e largura de uma parede em metros , calcule a area e a quatidade de tinta necessaria para pinta-la.
#Sabendo que cada litro de tinta pinta uma parede de 2m2.
# Area é calculada é base * altura 
larg = float(input('Digite a largura da parede ou a base: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
print('A área da parede corresponde a: {} m²'.format(area))
tinta = 2.0
tinta_nece = (larg*alt)/tinta
print('A quantidade de tinta necessaria para pintar a parede de {}m², é {} litros de tinta '.format(area,tinta_nece))