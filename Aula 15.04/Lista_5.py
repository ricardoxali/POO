print('Exercício 1')
def maior(x, y):
    if x > y:
        return x
    else:
        return y
    
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite um número: '))
print(maior(valor1, valor2))

print()

print('Exercício 2')
def maior(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite um número: '))
valor3 = int(input('Digite um número: '))
print(maior(valor1, valor2, valor3))

print()

print('Exercício 3')
def iniciais(nome):
    iniciais = []
    nome_completo = nome.split()
    for n in nome_completo:
        iniciais.append(n[:1])
    for n in iniciais:
        print(n, end = ' ')

seu_nome = input('Digite seu nome completo: ')
iniciais(seu_nome)

print()

print('Exercício 4')
def aprovado(nota1, nota2):
    return (nota1 + nota2) / 2 >= 60

nota1 = int(input('Digite a nota do primeiro bimestre'))
nota2 = int(input('Digite a nota do segundo bimestre'))
aprovado(nota1, nota2)

print()

print('Exercício 5')
def formatar_nome(nome):
    nome_completo = nome.split()
    nome_formatado = []
    for n in nome_completo:
        inicial = n[0].upper()
        resto = n[1:].lower()
        nome_formatado.append(inicial + resto)
    
    for x in nome_formatado:
        print(x, end = ' ')

seu_nome = input('Digite seu nome completo: ')
formatar_nome(seu_nome)