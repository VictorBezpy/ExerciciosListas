"""
10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.
"""
listaa = []
listab = []
listaab = []
for i in range(0, 20):
    a = int(input('Digite um número para A: '))
    listaa.append(a)
    listaab.append(a)
    b = int(input('Digite um número para B: '))
    listab.append(b)
    listaab.append(b)
print('A', listaa)
print('B', listab)
print('AB', listaab)
