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

print()

print('Exercício 9')
hora, minuto = input('Digite o horário no formato hh:mm\n').split(':')
hora = int(hora)
minuto = int(minuto)
if 0 <= hora < 24 and 0 <= minuto < 60:
    hora %= 12
    angulo = abs(11 * minuto - 60 * hora) / 2
    print()
    print(f'Menor ângulo entre os ponteiros = {min(angulo, 360 - angulo):.0f} graus')
else:
    print('Hora Inválida')

print()

print('Exercício 10')
dia, mes, ano = input('Digite uma data no formato dd/mm/aaaa\n').split('/')
dia, mes, ano = int(dia), int(mes), int(ano)
trinta = [4, 6, 9, 11]
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False
if mes < 1 or mes > 12:
    valido = False
elif mes in trinta:
    if dia < 1 or dia > 30:
        valido = False
    else:
        valido = True
elif mes == 2:
    if dia < 1 or (bissexto and dia > 29) or (not bissexto and dia > 28):
        valido = False
    else:
        valido = True
else:
    if dia < 1 or dia > 31:
        valido = False
    else:
        valido = True

if valido:
    print('A data informada é válida')
else:
    print('A data informada não é válida')