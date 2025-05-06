import math

print('Exercício 1 - Um Círculo')
class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return math.pi * self.raio ** 2
    def circunferencia(self):
        return 2 * math.pi * self.raio
    
x = Circulo()
x.raio = 10
print(f'Area = {x.area():.2f}')
print(f'Circunferencia = {x.circunferencia():.2f}')

print()

print('Exercício 2 - Uma Viagem')
class Viagem:
    def __init__(self):
        self.distancia = 0
        self.hora = 0
        self.minuto = 0
    def velocidade(self):
        tempo = self.hora + self.minuto / 60
        return self.distancia / tempo

x = Viagem()
x.distancia = 150
x.hora = 1
x.minuto = 30
print(f'Velocidade = {x.velocidade():.2f} km/h')

print()

print('Exercício 3 - Uma Conta Bancária')
class Conta:
    def __init__(self):
        self.titular = ''
        self.numero = ''
        self.saldo = 0
        self.deposito = 0
        self.saque = 0
    def operacao(self):
        return x.saldo + x.deposito - x.saque

x = Conta()
x.titular = 'Ricardo'
x.numero = '20241011110001'
x.saldo = 150
x.deposito = 200
x.saque = 50
print(f'Titular: {x.titular}')
print(f'Número da conta {x.numero}')
print(f'Saldo atual: {x.operacao()}')