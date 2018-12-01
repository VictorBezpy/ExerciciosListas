"""
12.Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que
determine quantos alunos com mais de 13 anos possuem altura inferior à média
de altura desses alunos.
"""
altura = []
idades = []

for k in range(0, 30):
    idade = int(input('Digite a idade do aluno: '))
    idades.append(idade)
    alt = float(input('Digite a altura  do aluno em cm: '))
    altura.append(alt)
k = 0
for i in range(0, 30):
    if idades[i] >= 13 and altura[i] < (sum(altura) / 30):
        k += 1
print('Alunos com mais de 13 anos e com altura inferior à média:', k)
