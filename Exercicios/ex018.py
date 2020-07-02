#ler um angulo e calcular o sen e cos
import math
angulo = float(input('Digite o angulo para calcularmos o seno e coseno : '))
coseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
print('o angulo de {}° possui o seno de {:.2f}° e coseno de {:.2f}°'.format(angulo,seno,coseno))
tangente = math.tan(math.radians(angulo))
print('A tangente é: {:.2f}° '.format(tangente))