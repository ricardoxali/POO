print('Exercício 1036 - Fórmula de Bhaskara')
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = b ** 2 - 4 * a * c
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    bhaskara1 = (- b + delta ** 0.5) / (2 * a)
    bhaskara2 = (- b - delta ** 0.5) / (2 * a)
    print(f'R1 = {bhaskara1:.5f}')
    print(f'R2 = {bhaskara2:.5f}')

print()

print('Exercício 1044 - Múltiplos')
a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Não sao Multiplos')
else:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

print()

print('Exercício 1049 - Animal')
subfilo = input()
classe = input()
ordem = input()
if subfilo == 'vertebrado':
    if classe == 'ave':
        if ordem == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if ordem == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if classe == 'inseto':
        if ordem == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if ordem == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')

print()

print('Exercício 1050 - DDD')
ddd = int(input())
if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')

print()

print('Exercício 2424 - Tira-Teima')
x, y = input().split()
x = int(x)
y = int(y)
if 0 <= x <= 432 and 0 <= y <= 468:
    print('dentro')
else:
    print('fora')

print()

print('Exercício 2670 - Máquina de Café')
A1 = int(input())
A2 = int(input())
A3 = int(input())
tempo1 = 2 * A2 + 4 * A3
tempo2 = 2 * A1 + 2 * A3
tempo3 = 4 * A1 + 2 * A2
print(min(tempo1, tempo2, tempo3))

print()

print('Exercício 1059 - Números Pares')
n = 2
while n <= 100:
    print(n)
    n += 2

print()

print('Exercício 1080 - Maior e Posição')
n = 1
ls = []
while n <= 100:
    x = int(input())
    ls.append(x)
    n += 1
maior = max(ls)
posicao = ls.index(maior)
print(maior)
print(posicao + 1)

print()

print('Exercício 1094 - Experiências')
e = int(input())
numero, cobaia = [], []
indice_coelho, indice_rato, indice_sapo = [], [], []
qntd_coelho, qntd_rato, qntd_sapo = [], [], []
while e > 0:
    n, c = input().split()
    n = int(n)
    numero.append(n)
    cobaia.append(c)
    e -= 1
total = sum(numero)
print(f'Total: {total} cobaias')

for i, cobaias in enumerate(cobaia):
    if cobaias == 'C':
        indice_coelho.append(i)
    elif cobaias == 'R':
        indice_rato.append(i)
    else:
        indice_sapo.append(i)

for i in indice_coelho:
    qntd_coelho.append(numero[i])
print(f'Total de coelhos: {sum(qntd_coelho)}')

for i in indice_rato:
    qntd_rato.append(numero[i])
print(f'Total de ratos: {sum(qntd_rato)}')

for i in indice_sapo:
    qntd_sapo.append(numero[i])
print(f'Total de sapos: {sum(qntd_sapo)}')

print(f'Percentual de coelhos: {(sum(qntd_coelho) / total) * 100:.2f} %')
print(f'Percentual de ratos: {(sum(qntd_rato) / total) * 100:.2f} %')
print(f'Percentual de sapos: {(sum(qntd_sapo) / total) * 100:.2f} %')

print()

print('Exercício 1114 - Senha Fixa')
tentativa = 0
while tentativa != 2002:
    tentativa = int(input())
    if tentativa == 2002:
        print('Acesso Permitido')
    else:
        print('Senha Invalida')

print()

print('Exercício 1116 - Dividindo X por Y')
n = int(input())
while n > 0:
    x, y = input().split()
    x, y = int(x), int(y)
    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x / y:.1f}')
    n -= 1

print()

print('Exercício 1151 - Fibonacci Fácil')
n = int(input())
a = 0
b = 1
while n > 0:
    if n == 1:
        print(a)
    else:
        print(a, end = ' ')
    proximo = a + b
    a = b
    b = proximo
    n -= 1