"""
7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.
"""
lista = []
for i in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
print('Soma:', sum(lista))

print('Multiplicação:', (lista[0] * lista[1] * lista[2] * lista[3] * lista[4]))

print('Números digitados:', lista)
