"""
11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
listaa = []
listab = []
listac = []
listaabc = []
for i in range(0, 10):
    a = int(input('Digite um número para A: '))
    listaa.append(a)
    listaabc.append(a)
    b = int(input('Digite um número para B: '))
    listab.append(b)
    listaabc.append(b)
    c = int(input('Digite um número para C: '))
    listac.append(c)
    listaabc.append(c)
print('A', listaa)
print('B', listab)
print('C', listac)
print('ABC', listaabc)
