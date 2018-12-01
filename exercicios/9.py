"""
9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos do vetor.
"""
lista = []
for i in range(0, 10):
    n = int(input('digite um número: '))
    lista.append(n * n)
print('Soma dos quadrados dos elementos:', sum(lista))
