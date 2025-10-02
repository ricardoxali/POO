import json
from datetime import date, datetime

class Jogo:
    def __init__(self, i, n, e, d):
        self.__id = i
        self.__nome = n
        self.__empresa = e
        d, m, a = d.strip('/')
        self.__data = date(a, m, d)
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_empresa(self): return self.__empresa
    def get_data(self): return self.__data
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__empresa} - {self.__data.day}/{self.__data.month}/{self.__data.year}"
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "empresa":self.__empresa, "data":self.__data}
        return dic
    @staticmethod
    def from_json(dic):
        return Jogo(dic["id"], dic["nome"], dic["empresa"], dic["data"])

class Jogos:
    __jogos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.__jogos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__jogos
    @classmethod
    def listar_id(cls, i):
        cls.abrir()
        for j in cls.__jogos:
            if j.get_id() == i:
                return j
    @classmethod
    def maisnovos(cls):
        cls.abrir()
        datas, jogos = [], []
        for j in cls.__jogos:
            datas.append(j.get_data())
        datas.sort(reverse=True)
        for d in datas:
            for j in cls.__jogos:
                if j.get_data() == d:
                    jogos.append(j)
        return jogos
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        ind = cls.__jogos.index(obj)
        cls.__jogos.pop(ind)
        cls.__jogos.insert(ind, obj)
        cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir
        ind = cls.__jogos.index(obj)
        cls.__jogos.pop(ind)
        cls.salvar()
    @classmethod
    def abrir(cls):
        cls.__jogos = []
        try:
            with open("jogos.json", mode="r") as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Jogo.from_json(dic)
                    cls.__jogos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open("jogos.json", mode="w") as arq:
            json.dump(cls.__jogos, arq, default = Jogo.to_json)

class UI:
    @staticmethod
    def main():
        op = UI.menu()
        if op == 1: UI.listar()
        if op == 2: UI.inserir()
        if op == 3: UI.atualizar()
        if op == 4: UI.excluir()
        if op == 5: UI.maisnovos()
    @staticmethod
    def menu():
        print("1 - Listar, 2 - Inserir, 3 - Atualizar, 4 - Excluir, 5 - Mais Novos")
        op = int(input())
        return op
    @staticmethod
    def listar():
        jogos = Jogos.listar()
        for j in jogos:
            print(j)
    @staticmethod
    def inserir():
        id = int(input('Informe o id: '))
        nome = input('Informe o nome: ')
        empresa = input('Informe a empresa: ')
        data = input('Informe a data: ')
        Jogos.inserir(Jogo(id, nome, empresa, data))
    @staticmethod
    def atualizar():
        id = int(input('Informe o id cadastrado do jogo: '))
        nome = input('Informe o novo nome: ')
        empresa = input('Informe a nova empresa: ')
        data = input('Informe a nova data: ')
        Jogos.atualizar(Jogo(id, nome, empresa, data))
    @staticmethod
    def excluir():
        id = int(input('Informe o id do jogo: '))
        Jogos.excluir(Jogo(id, 'n', 'e', '1/1/2000'))
    @staticmethod
    def maisnovos():
        jogos = Jogos.maisnovos()
        for j in jogos:
            print(j)

UI.main()