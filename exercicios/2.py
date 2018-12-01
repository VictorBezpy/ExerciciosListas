"""
2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem
inversa.
"""
lista = []
k = 0
while k < 10:
    l = float(input('digite um real inteiro: '))
    lista.append(l)
    k += 1
print(lista[::-1])
