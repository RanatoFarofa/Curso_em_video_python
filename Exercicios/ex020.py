#sotear a ordem dos trabalho dos quatro alunos
import random
n1 = (input('Aluno digite seu nome: '))
n2 = (input('Aluno digite seu nome: '))
n3 = (input('Aluno digite seu nome: '))
n4 = (input('Aluno digite seu nome: '))
alunos = [n1,n2,n3,n4]
sorteio = random.choice(alunos)
#ordem = sorted(alunos)
random.shuffle(alunos)
print('O aluno sorteado para apagar o quadro é: ',sorteio)
print(' A ordenação para apagar se o {} não concordar com o serteio será : {} '.format(sorteio,alunos))
