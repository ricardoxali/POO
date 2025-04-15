#Exercício 1
nome = input("Digite seu nome completo:\n")
primeiro_nome = nome.split()[0]
print(f'Bem vindo(a) ao Python, {primeiro_nome}')

print()

#Exercício 2
nota1 = int(input("Digite a nota do primeiro bimestre da disciplina:\n"))
nota2 = int(input("Digite a nota do segundo bimestre da disciplina:\n"))
media = (nota1 * 2 + nota2 * 3) / 5
print(f'Média parcial = {media:.0f}')

print()

#Exercício 3
print('Digite a base e a altura do retângulo')
base = int(input())
altura = int(input())
area = base * altura
perimetro = 2 * base + 2 * altura
diagonal = (base ** 2 + altura ** 2) ** (1/2)
print(f'Área  = {area:.2f} - Perímetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}')

print()

#Exercício 4
frase = input('Digite uma frase:\n')
ultima = frase[frase.rindex(' ') + 1:]
print(ultima)