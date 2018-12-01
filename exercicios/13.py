"""
13.Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []
k = 1
for i in range(0, 12):
    t = float(input('Digite a média de temperatura do mês %d:' % k))
    k += 1
    temperatura.append(t)
print('Meses com temperaturas acima da média anual:')
for c in range(0, 12):
    if temperatura[c] >= (sum(temperatura) / 12):
        print(meses[temperatura.index(temperatura[c])], ':', temperatura[c])
