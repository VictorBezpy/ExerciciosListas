"""
14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente".
"""
k = 0
a = str(input("Telefonou para a vítima? s-sim n-não: "))
if a == 's':
    k += 1
b = str(input("Esteve no local do crime? s-sim n-não: "))
if b == 's':
    k += 1
c = str(input("Mora perto da vítima? s-sim n-não: "))
if c == 's':
    k += 1
d = str(input("Devia para a vítima? s-sim n-não: "))
if d == 's':
    k += 1
e = str(input("Já trabalhou com a vítima? s-sim n-não: "))
if e == 's':
    k += 1
if k >= 1 and k <= 2:
    print("Suspeita")
if k >= 3 and k <= 4:
    print("Cúmplice")
if k == 5:
    print("Assassino")
if k == 0:
    print("Inocente")
