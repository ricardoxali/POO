print('Questão 1')
class Viagem:
    def __init__(self, de, di, co):
        self.SetDestino(de)
        self.SetDistancia(di)
        self.SetCombustivel(co)
    def SetDestino(self, v):
        if v == '': raise ValueError('O destino não pode ser vazio')
        self.__destino = v
    def SetDistancia(self, v):
        if v <= 0: raise ValueError('A distância deve ser maior que zero')
        self.__distancia = v
    def SetCombustivel(self, v):
        if v <= 0: raise ValueError('O consumo de combústivel deve ser maior que zero')
        self.__combustivel = v
    def GetDestino(self): return self.__destino
    def GetDistancia(self): return self.__distancia
    def GetCombustivel(self): return self.__combustivel
    def Consumo(self): return self.GetDistancia() / self.GetCombustivel()
    def ToString(self): return f'A viagem para {self.GetDestino()} terá um consumo de aproximadamente {self.Consumo():.2f} km/L'

class ViagemUI:
    @staticmethod
    def menu():
        op = int(input('1 - Calcular, 2 - Fim\n'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
    @staticmethod
    def calculo():
        de = input('Informe o destino da viagem: ')
        di = int(input('Informe a distância percorrida da viagem em km: '))
        co = int(input('Informe a quantidade de combustível gasta em litros: '))
        x = Viagem(de, di, co)
        print(x.ToString())

ViagemUI.main()

print()

print('Questão 2')
class Pais:
    def __init__(self, n, h, a):
        self.SetNome(n)
        self.SetHabitantes(h)
        self.SetArea(a)
    def SetNome(self, v):
        if v == '': raise ValueError('O nome não pode ser vazio')
        self.__nome = v
    def SetHabitantes(self, v):
        if v <= 0: raise ValueError('O número de habitantes deve ser maior que zero')
        self.__habitantes = v
    def SetArea(self, v):
        if v <= 0: raise ValueError('A área deve ser maior que zero')
        self.__area = v
    def GetNome(self): return self.__nome
    def GetHabitantes(self): return self.__habitantes
    def GetArea(self): return self.__area
    def Densidade(self): return self.GetHabitantes() / self.GetArea()
    def ToString(self): return f'A densidade demográfica de {self.GetNome()} é de {self.Densidade()} hab./km²'

class PaisUI:
    @staticmethod
    def menu():
        op = int(input('1 - Calcular, 2 - Fim\n'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1: PaisUI.calculo()
    @staticmethod
    def calculo():
        n = input('Informe o nome do páis: ')
        h = int(input('info'))