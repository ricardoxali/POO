print('Exercício 1')
print('Digite dois valores inteiros')
a = int(input())
b = int(input())
if a > b:
    maior = a
elif a < b:
    maior = b
else:
    maior = 'Números iguais'
print()
print(f'Maior = {maior}')

print()

print('Exercício 2')
print('Digite quatro valores inteiros')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
ls = [a, b, c, d]
media = sum(ls) / 4
print()
print(f'Média = {media}')
print('Números menores que à média')
for n in ls:
    if n < media:
        print(n)
print('Números maiores ou iguais à média')
for n in ls:
    if n >= media:
        print(n)

print()

print('Exercício 3')
print('Digite quatro valores inteiros')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
ls = [a, b, c, d]
pares, impares = [], []
for n in ls:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print()
print(f'Soma dos pares = {sum(pares)}')
print(f'Soma dos ímpares = {sum(impares)}')

print()

print('Exercício 4')
horas, minutos = [], []
print('Digite o primeiro horário no formato hh:mm')
hora, minuto = input().split(':')
horas.append(int(hora))
minutos.append(int(minuto))
print('Digite o segundo horário no formato hh:mm')
hora, minuto = input().split(':')
horas.append(int(hora))
minutos.append(int(minuto))
minutos_total = sum(minutos)
if minutos_total >= 60:
    horas.append(minutos_total // 60)
    minutos_total = minutos_total % 60
horas_total = sum(horas)
print()
print(f'Total de horas = {horas_total}:{minutos_total}')

print()

print('Exercício 5')
meses = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}
a = input('Digite o número do mês:\n')
n = int(a)
if n < 4:
    trimestre = 'primeiro'
elif n < 7:
    trimestre = 'segundo'
elif n < 10:
    trimestre = 'terceiro'
else:
    trimestre = 'quarto'
print()
print(f'O mês de {meses[a]} é do {trimestre} trimestre do ano')

print()

print('Exercício 6')
a = int(input('Digite três valores inteiros\n'))
b = int(input())
c = int(input())
maior = max(a, b, c)
menor = min(a, b, c)
print()
print(f'A soma do maior com o menor número é {maior + menor}')

print()

print('Exercício 7')
a = int(input('Digite os coeficientes a, b e c de uma equação do segundo grau\n'))
b = int(input())
c = int(input())
delta = b ** 2 - 4 * a * c
if a == 0 or delta < 0:
    print('impossível calcular')
else:
    r1 = (-b + delta ** 0.5) / 2 * a
    r2 = (-b - delta ** 0.5) / 2 * a
    print()
    print(f'As raízes são {r1} e {r2}')

print()

print('Exercício 8')
a = int(input('Digite quatro valores inteiros\n'))
b = int(input())
c = int(input())
d = int(input())
ls = [a, b, c, d]
if a == b or a == c or a == d or b == c or b == d or c == d:
    print('Erro')
else:
    maior = max(ls)
    menor = min(ls)
    ls.remove(maior, menor)
    print()
    print(f'Maior valor = {maior}')
    print(f'Menor valor = {menor}')
    print(f'A soma do segundo maior valor com o segundo menor = {sum(ls)}')