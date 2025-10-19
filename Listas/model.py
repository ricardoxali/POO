from datetime import datetime
import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha":self.__senha}
        return dic
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

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
        if v < 0:
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
    def __str__(self): return f"{self.get_id()} - {self.get_desc()} - R$ {self.get_valor():.2f}"
    def to_json(self):
        dic = {"id":self.__id, "desc":self.__desc, "valor":self.__valor}
        return dic
    @staticmethod
    def from_json(dic): return Servico(dic["id"], dic["desc"], dic["valor"])

class Horario:
    def __init__(self, i, d):
        self.set_id(i)
        self.set_data(d)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_profissional(0)
    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional
    def __str__(self): return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
    def to_json(self):
        dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"),
        "confirmado":self.__confirmado, "id_cliente":self.__id_cliente,
        "id_servico":self.__id_servico, "id_profissional":self.__id_profissional}
        return dic
    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_cliente(dic["id_cliente"])
        horario.set_id_servico(dic["id_servico"])
        horario.set_id_profissional(dic["id_profissional"])
        return horario

class Profissional:
    def __init__(self, id, nome, espec, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(espec)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_especialidade(self, espec): self.__especialidade = espec
    def set_conselho(self, conselho): self.__conselho = conselho
    def set_email(self, email): self.__email = email
    def set_senha(self, senha): self.__senha = senha
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho}"
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "especialidade":self.__especialidade, "conselho":self.__conselho, "email":self.__email, "senha":self.__senha}
        return dic
    @staticmethod
    def from_json(dic):
        profissional = Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])
        return profissional

class ClienteDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = -1 # Assim o admin vai ter id 0 e os outros clientes terão id a partir do 1
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
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos: 
            if obj.get_id() == id: return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls.__objetos.index(aux)
            cls.__objetos[index] = obj
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cliente.to_json)

class ServicoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
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
        for obj in cls.__objetos: 
            if obj.get_id() == i: return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls.__objetos.index(aux)
            cls.__objetos[index] = obj
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
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

class HorarioDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
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
        for obj in cls.__objetos:
            if obj.get_id() == i:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls.__objetos.index(aux)
            cls.__objetos[index] = obj
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open('horarios.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('horarios.json', mode='w') as arq:
            json.dump(cls.__objetos, arq, default=Horario.to_json)

class ProfissionalDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
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
        for obj in cls.__objetos:
            if obj.get_id() == i:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            index = cls.__objetos.index(aux)
            cls.__objetos[index] = obj
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open('profissional.json', mode='r') as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open('profissional.json', mode='w') as arq:
            json.dump(cls.__objetos, arq, default=Profissional.to_json)