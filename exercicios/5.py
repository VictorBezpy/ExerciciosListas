"""
5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""
vetor = []
i = 1
par = []
imp = []
while i <= 20:
    n = int(input('Digite um número: '))
    vetor.append(n)
    i += 1
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
print('números digitados', vetor)
print('números pares', par)
print('números impares', imp)
