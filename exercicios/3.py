"""
3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
lista = []
k = 0
while k < 4:
    l = int(input('digite a nota: '))
    lista.append(l)
    k += 1
print(lista)
print('Média:', sum(lista) / 4)
