"""
8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem
inversa a ordem lida.
"""
idade = []
altura = []
k = 0

while k <= 4:
    i = int(input('Digite a idade: '))
    idade.append(i)
    alt = float(input('Digite a altura: '))
    altura.append(alt)
    k += 1
print('Idades:', idade[::-1])
print('Alturas:', altura[::-1])
