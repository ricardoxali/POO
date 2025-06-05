print('Questão 1 - Um Retângulo')
class Retangulo:
    def __init__(self, b, h):
        self.SetBase(b)
        self.SetAltura(h)
    def SetBase(self, v):
        if v <= 0: raise ValueError('O valor tem que ser positivo')
        self.__b = v
    def SetAltura(self, v):
        if v <= 0: raise ValueError('O valor tem que ser positivo')
        self.__h = v
    def GetBase(self): return self.__b
    def GetAltura(self): return self.__h
    def CalcArea(self): return self.GetBase() * self.GetAltura()
    def CalcDiagonal(self): return (self.GetBase() ** 2 + self.GetAltura() ** 2) ** 0.5
    def ToString(self): return f'O retângulo de base {self.GetBase()} e altura {self.GetAltura()} tem área de {self.CalcArea()} e diagonal de {self.CalcDiagonal():.2f}'

b = int(input('Base: '))
h = int(input('Altura: '))
x = Retangulo(b, h)
print(x.ToString())

print()

print('Questão 2 - Um Frete')
class Frete:
    def __init__(self, distancia, peso):
        if distancia < 0 or peso < 0: raise ValueError('O valor não pode ser negativo')
        self.SetDistancia(distancia)
        self.SetPeso(peso)
    def SetDistancia(self, v):
        if v < 0: raise ValueError('O valor não pode ser negativo')
        self.__d = v
    def SetPeso(self, v):
        if v < 0: raise ValueError('O valor não pode ser negativo')
        self.__p = v
    def GetDistancia(self): return self.__d
    def GetPeso(self): return self.__p
    def CalcFrete(self): return self.GetPeso() * self.GetDistancia() * 0.01
    def ToString(self): return f'O frete cobrado pelo transporte de {self.GetPeso()} kg por {self.GetDistancia()} km será de R$ {self.CalcFrete():.2f}'

distancia = int(input('Distância (km): '))
peso = int(input('Peso (kg): '))
x = Frete(distancia, peso)
print(x.ToString())

print()

print('Questão 3 - Uma Equação do II Grau')
class ESG: #Equação do Segundo Grau
    def __init__(self, a, b, c):
        self.SetA(a)
        self.SetB(b)
        self.SetC(c)
    def SetA(self, v):
        if v == 0: raise ValueError('O coeficiente não pode ser nulo')
        self.__a = v
    def SetB(self, v):
        self.__b = v
    def SetC(self, v):
        self.__c = v
    def GetA(self): return self.__a
    def GetB(self): return self.__b
    def GetC(self): return self.__c
    def Delta(self): return self.GetB() ** 2 - 4 * self.GetA() * self.GetC()
    def TemRaizesReais(self): return self.Delta() >= 0 and self.GetA() != 0
    def Raiz1(self): 
        if self.TemRaizesReais(): return (-self.GetB() + self.Delta() ** 0.5) / (2 * self.GetA())
    def Raiz2(self): 
        if self.TemRaizesReais(): return (-self.GetB() - self.Delta() ** 0.5) / (2 * self.GetA())
    def ToString(self):
        if self.TemRaizesReais(): return f'As raízes da equação do segundo grau cujos coeficientes a, b e c são, respectivamente, {self.GetA()}, {self.GetB()} e {self.GetC()} são {self.Raiz1():.2f} e {self.Raiz2():.2f}'
        else: return f'A equação do segundo grau cujos coeficientes a, b e c são, respectivamente, {self.GetA()}, {self.GetB()} e {self.GetC()} não possui raízes reais'
    
a = int(input('Coeficiente a: '))
b = int(input('Coeficiente b: '))
c = int(input('Coeficiente c: '))
x = ESG(a, b, c)
print(x.ToString())