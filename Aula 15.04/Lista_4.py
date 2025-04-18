print('Exercício 1036 - Fórmula de Bhaskara')
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = b ** 2 - 4 * a * c
if a == 0 or delta < 0:
    print('Impossível calcular')
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
        print('São Múltiplos')
    else:
        print('Não São Múltiplos')
else:
    if b % a == 0:
        print('São Múltiplos')
    else:
        print('Não São Múltiplos')

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

print('Exercício')