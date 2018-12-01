"""
15.Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for informado um
valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do
outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
notas = []
while -1 not in notas:
    n = int(input('Digite um número real: '))
    notas.append(n)
del notas[-1]
print('Quantidade de valores lidos:', len(notas))
print('Valores informados:', notas)
print('Valores na ordem inversa e em coluna:', )
x = 0
notas.reverse()
while x <= (len(notas) - 1):
    print(notas[x])
    x += 1
print('Soma dos valores:', sum(notas))
print('Média dos valores:', (sum(notas) / len(notas)))
x = 0
k = 0
while x <= (len(notas) - 1):
    if notas[x] > (sum(notas) / len(notas)):
        k += 1
    x += 1
print('Quantidade de valores acima da média:', k)
x = 0
k = 0
while x <= (len(notas) - 1):
    if notas[x] < 7:
        k += 1
    x += 1
print('Quantidade de valores abaixo de 7:', k)
print('ACABOU!!!')
