from datetime import date, timedelta
class Treino:
    def __init__(self, i, da, di, t):
        self.SetId(i)
        self.SetData(da)
        self.SetDist(di)
        self.SetTemp(t)
    def SetId(self, v):
        try:
            v = int(v)
        except ValueError:
            raise ValueError('O ID deve ser um número inteiro')
        if v < 0: raise ValueError('O ID não pode ser negativo')
        self.__id = v
    def SetData(self, v):
        # bissexto = False
        # if ano % 4 == 0 or (ano % 100 == 0 and ano % 4 == 0): bissexto = True
        # meses_30 = [4, 6, 9, 11]
        # ano, mes, dia = map(int, v.split('/'))
        # hoje = date.today()
        # ah, mh, dh = hoje.year(), hoje.month(), hoje.day()
        # if (ano > ah) or (mes > mh) or (dia > dh): raise ValueError('Data Inválida')
        # if mes == 2:
        #     if bissexto:
        #         if dia > 29: raise ValueError('Data Inválida')
        #     else:
        #         if dia > 28: raise ValueError('Data Inválida')
        # elif mes in meses_30:
        #     if dia > 30: raise ValueError('Data Inválida')
        # else:
        #     if dia > 31: raise ValueError('Data Inválida')
        # self.__data = date(ano, mes, dia)
        ano, mes, dia = map(int, v.split('/'))
        hoje = date.today()
        try:
            self.__data = date(ano, mes, dia)
        except ValueError:
            raise ValueError('Data Inexistente')
        if self.__data > hoje: raise ValueError('Data Futura')
    def SetDist(self, v):
        try:
            v = float(v)
        except ValueError:
            raise ValueError('A distância deve ser um número')
        if v <= 0: raise ValueError('A distância deve ser um valor positivo')
        self.__dist = v
    def SetTemp(self, v):
        try:
            h, m, s = map(int, v.split(':'))
        except ValueError:
            raise ValueError('Tempo Inválido')
        if h < 0 or not (0 <= m < 60) or not (0 <= s < 60):
            raise ValueError('Tempo Inválido')
        self.__temp = timedelta(hours=h, minutes=m, seconds=s)
    def GetId(self): return self.__id
    def GetData(self): return self.__data
    def GetDist(self): return self.__dist
    def GetTemp(self): return self.__temp
    def Velocidade(self): return self.__dist / (self.__temp.total_seconds() / 3600)
    def __str__(self): return f"ID: {self.GetId()} - Data: {self.GetData().strftime('%d/%m/%Y')} - Distância: {self.GetDist()} - Tempo: {self.GetTemp()} - Velocidade: {self.Velocidade()} km/h"

class TreinoUI:
    __treinos = []
    @staticmethod
    def Main():
        op = 0
        while op != 7:
            op = TreinoUI.Menu()
            if op == 1: TreinoUI.Inserir()
            if op == 2: TreinoUI.Listar()
            if op == 3: TreinoUI.Listar_Id()
            if op == 4: TreinoUI.Atualizar()
            if op == 5: TreinoUI.Excluir()
            if op == 6: TreinoUI.MaisRapido()
    @staticmethod
    def Menu():
        op = int(input('1-Inserir Novo Treino, 2-Listar Todos os Treinos, 3-Listar Treino Específico, 4-Atualizar Treino, 5-Excluir Treino, 6-Treino Mais Rápido, 7-Sair'))
        return op
    @classmethod
    def Inserir(cls):
        id = input('Digite o ID: ')
        dt = input('Digite a data do treino: ')
        di = input('Digite a distância percorrida: ')
        te = input('Digite o tempo gasto: ')
        t = Treino(id, dt, di, te)
        cls.__treinos.append(t)
    @classmethod
    def Listar(cls):
        for t in cls.__treinos:
            print(t)
    @classmethod
    def Listar_Id(cls):
        i = int(input('Digite o ID do treino: '))
        for t in cls.__treinos:
            if t.GetId() == i:
                print(t)
    @classmethod
    def Atualizar(cls):
        i = int(input('Digite o ID do treino: '))
        for t in cls.__treinos:
            if t.GetId() == i:
                n = cls.__treinos.index(t)
                id = input('Digite o ID: ')
                dt = input('Digite a data do treino: ')
                di = input('Digite a distância percorrida: ')
                te = input('Digite o tempo gasto: ')
                tr = Treino(id, dt, di, te)
                cls.__treinos.pop(n)
                cls.__treinos.insert(n, tr)
    @classmethod
    def Excluir(cls):
        i = int(input('Digite o ID do treino: '))
        for t in cls.__treinos:
            if t.GetId() == i:
                cls.__treinos.remove(t)
    @classmethod
    def MaisRapido(cls):
        velocidades = []
        for t in cls.__treinos:
            velocidades.append(t.Velocidade())
        maior = max(velocidades)
        for t in cls.__treinos:
            if t.Velocidade() == maior:
                print(t)

TreinoUI.main()