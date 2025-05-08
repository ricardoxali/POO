print('Exercício 1')
print('1) 11')
print('2) -10')
print('3) 12.5')
print('4) 4')
print('5) 2.5')

print()

print('Exercício 2')
a, b, c = input('Digite três números inteiros separados por espaços:\n').split()
a, b, c = int(a), int(b), int(c)
ls = [a, b, c]
soma = 0
for x in ls:
    if x % 2 == 0:
        soma += x
print(f'Soma dos pares = {soma}')

print()

print('Exercício 3')
frase = input('Escreva uma frase\n')
ls = []
retira = 1  # Vamos começar com a posição 1
for x in frase:
    if retira % 2 == 1:
        ls.append(x)
    retira += 1
print(''.join(ls))

print()

print('Exercíco 4')
class Agua():
    mes = 0
    ano = 0
    consumo = 0