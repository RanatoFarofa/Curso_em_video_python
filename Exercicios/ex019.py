#sotear algum dos 4 alunos 
import random
n1 = str(input('Aluno digite seu nome: '))
n2 = str(input('Aluno digite seu nome: '))
n3 = str(input('Aluno digite seu nome: '))
n4 = str(input('Aluno digite seu nome: '))
alunos = [n1,n2,n3,n4]
sorteio = random.choice(alunos)
print('O aluno sorteado para apagar o quadro é: ',sorteio)