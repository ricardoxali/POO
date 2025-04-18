print('Exercício 1004 - Produto Simples')
valor1 = int(input())
valor2 = int(input())
PROD = valor1 * valor2
print(f'PROD = {PROD}')

print()

print('Exercício 1005 - Média 1')
nota1 = float(input())
nota2 = float(input())
MEDIA = (nota1 * 3.5 + nota2 * 7.5) / 11
print(f'MEDIA = {MEDIA:.5f}')

print()

print('Exercício 1011 - Esfera')
raio = float(input())
pi = 3.14159
VOLUME = (4 / 3) * pi * raio ** 3
print(f'VOLUME = {VOLUME:.3f}')

print()

print('Exercício 2416 - Corrida')
distancia, comprimento = input().split()
distancia = int(distancia)
comprimento = int(comprimento)
print(distancia % comprimento)

print()

print('Exercício 1015 - Distância entre dois pontos')
x1, y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
print(f'{distancia:.4f}')

print()

print('Exercício 1930 - Tomadas')
T1, T2, T3, T4 = input().split()
T1 = int(T1)
T2 = int(T2)
T3 = int(T3)
T4 = int(T4)
aparelhos = T1 + T2 + T3 + T4 - 3
print(aparelhos)