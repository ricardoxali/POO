print('Questão 1')
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
    def CalcArea(self): return self.__b * self.__h
    def CalcDiagonal(self): return (self.__b ** 2 + self.__h ** 2) ** 0.5
    def ToString(self): return f'O retângulo de base {self.GetBase()} e altura {self.GetAltura()} tem área de {self.CalcArea()} e diagonal de {self.CalcDiagonal():.2f}'

b = int(input('Base: '))
h = int(input('Altura: '))
x = Retangulo(b, h)
print(x.ToString())

print()

print('Questão 2')
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