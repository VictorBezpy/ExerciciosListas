"""
6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
num vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.
"""

lista = []
for i in range(1, 11):
    soma = 0
    for c in range(1, 5):
        n = float(input('Digite a nota(%d) do aluno(%d):' % (c, i)))
        soma += n
    lista.append(soma / 4)
aprovados = 0
for k in range(0, 10):
    if lista[k] >= 7:
        aprovados += 1
print('%d alunos foram aprovados com média maior que 7.' % aprovados)
