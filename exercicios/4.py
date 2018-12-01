"""
4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.
"""
letras = []
i = 1
while i <= 10:
    letras.append(input("letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    if letras[i] not in 'aeiou':
        cont += 1
    i += 1
print("foram lidas %d consoantes" % cont)
