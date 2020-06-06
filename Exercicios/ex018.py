#ler um angulo e calcular o sen e cos
import math
angulo = float(input('Digite o angulo para calcularmos o seno e coseno : '))
coseno = math.cos(angulo)
seno = math.sin(angulo)
print('o angulo de {}° possui o seno de {:.4f}° e coseno de {:.4f}°'.format(angulo,seno,coseno))