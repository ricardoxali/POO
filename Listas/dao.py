from model import Cliente, Servico, Horario, Profissional
from abc import ABC, abstractmethod
import json

class DAO(ABC):
    _objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls._objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls._objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls._objetos
    @classmethod
    def listar_id(cls, i):
        cls.abrir()
        for obj in cls._objetos: 
            if obj.get_id() == i: return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls._objetos.index(aux)
            cls._objetos[index] = obj
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls.salvar()
    @classmethod
    @abstractmethod
    def abrir():
        pass
    @classmethod
    @abstractmethod
    def salvar():
        pass

class ClienteDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = -1
        for aux in cls._objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls._objetos.append(obj)
        cls.salvar()
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=lambda obj:obj.to_json())

class ServicoDAO(DAO):
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open('servicos.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('servicos.json', mode='w') as arq:
            json.dump(cls._objetos, arq, default=lambda obj:obj.to_json())

class HorarioDAO(DAO):
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls._objetos.remove(aux)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open('horarios.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('horarios.json', mode='w') as arq:
            json.dump(cls._objetos, arq, default=lambda obj:obj.to_json())

class ProfissionalDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open('profissional.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('profissional.json', mode='w') as arq:
            json.dump(cls._objetos, arq, default=lambda obj:obj.to_json())    