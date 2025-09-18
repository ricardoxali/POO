import json
class Servico:
    def __init__(self, i, d, v):
        self.set_id(i)
        self.set_desc(d)
        self.set_valor(v)
    def set_id(self, v):
        try:
            v = int(v)
        except ValueError:
            raise ValueError('O id deve ser um número inteiro positivo')
        if v <= 0:
            raise ValueError('O id deve ser um número inteiro positivo')
        self.__id = v
    def set_desc(self, v):
        try:
            v = float(v)
        except ValueError:
            self.__desc = v
        else:
            raise ValueError('A descrição não pode ser numérica')
    def set_valor(self, v):
        try:
            v = float(v)
        except ValueError:
            raise ValueError('O valor deve ser numérico')
        if v <= 0:
            raise ValueError('O valor deve ser positivo')
        self.__valor = v
    def get_id(self): return self.__id
    def get_desc(self): return self.__desc
    def get_valor(self): return self.__valor
    def __str__(self): return f"{self.get_id()} - {self.get_desc()} - {self.get_valor():.2f}"
    def to_json(self):
        dic = {"id":self.__id, "desc":self.__desc, "desc":self.__valor}
        return dic
    @staticmethod
    def from_json(dic): return Servico(dic["id"], dic["desc"], dic["valor"])

class ServicoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    @classmethod
    def listar_id(cls, i):
        cls.abrir()
        for s in cls.__objetos:
            if s.get_id() == i:
                return s
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls.__objetos.index(aux)
            cls.__objetos[index] = obj
            cls.__objetos.sort(key=lambda o: o.get_id())
            cls.salvar()
    @classmethod
    def excluir(cls, i):
        cls.abrir()
        for s in cls.__objetos:
            if s.get_id() == i:
                aux = cls.__objetos.index(s)
                cls.__objetos.pop(aux)
        cls.salvar()
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open('servicos.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('servicos.json', mode='w') as arq:
            json.dump(cls.__objetos, arq, default=Servico.to_json)