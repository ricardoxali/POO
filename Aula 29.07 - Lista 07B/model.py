from datetime import date
import json
class Contato:
    def __init__(self, i, no, e, f, na):
        self.__id = i
        self.__nome = no
        self.__email = e
        self.__fone = f
        self.__nasc = na
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.day:02d}/{self.__nasc.month:02d}/{self.__nasc.year}"

class ContatoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        cls.__objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    @classmethod
    def listar_id(cls, i):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_id() == i:
                return c
    @classmethod
    def atualizar(cls, i, obj):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_id() == i:
                ind = cls.__objetos.index(c)
                cls.__objetos.pop(ind)
                cls.__objetos.insert(ind, obj)
        cls.salvar()
    @classmethod
    def excluir(cls, i):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_id() == i:
                cls.__objetos.remove(c)
        cls.salvar()
    @classmethod
    def pesquisar(cls, i):
        cls.abrir()
        contatos = []
        for c in cls.__objetos:
            if c.get_nome().lower().startswith(i):
                contatos.append(c)
        return contatos
    @classmethod
    def aniversariantes(cls, i):
        meses = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
        }
        aniver = []
        try:
            i = int(i)
        except ValueError:
            i = meses[i.lower()]
        for c in cls.__objetos:
            nasc = c.get_nasc()
            if nasc.month == i:
                aniver.append(f'{c.get_nome()}: {nasc.day:02d}/{nasc.month:02d}')
        return aniver
    @classmethod
    def abrir(cls):
        cls.__objetos = []
        with open('contatos.json', mode='r') as arq:
            contatos = json.load(arq)
            for dic in contatos:
                d, m, a = map(int, dic['_Contato__nasc'].split('/'))
                obj = Contato(
                    dic['_Contato__id'],
                    dic['_Contato__nome'],
                    dic['_Contato__email'],
                    dic['_Contato__fone'],
                    date(a, m, d)
                    )
                cls.__objetos.append(obj)
    @classmethod
    def salvar(cls):
        x = []
        for c in cls.__objetos:
            dic = vars(c).copy()
            nasc = c.get_nasc()
            dic['_Contato__nasc'] = f'{nasc.day:02d}/{nasc.month:02d}/{nasc.year}'
            x.append(dic)
        with open('contatos.json', mode='w') as arq:
            json.dump(x, arq, default=vars)