from datetime import date
class Contato:
    def __init__(self, i, no, e, f, na):
        self.__id = i
        self.__nome = no
        self.__email = e
        self.__fone = f
        d, m, a = map(int, na.split('/'))
        self.__nasc = date(a, m, d)
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_nasc(self): return self.__nasc
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc}"

class ContatoUI:
    __contatos = []
    @staticmethod
    def menu():
        op = int(input('1-Inserir, 2-Listar, 3-Listar Específico, 4-Atualizar, 5-Excluir, 6-Pesquisar, 7-Aniversariantes, 8-Abrir, 9-Salvar, 10-Sair'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniversariantes()
            if op == 8: ContatoUI.abrir()
            if op == 9: ContatoUI.salvar()
    @classmethod
    def inserir(cls):
        i = int(input('Digite o ID: '))
        no = input('Digite o nome: ')
        e = input('Digite o email: ')
        f = input('Digite o telefone: ')
        na = input('Digite a data de nascimento: ')
        x = Contato(i, no, e, f, na)
        cls.__contatos.append(x)
    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)
    @classmethod
    def listar_id(cls):
        i = input('Digite o ID do contato: ')
        for c in cls.__contatos:
            if c.get_id() == i:
                print(c)
    @classmethod
    def atualizar(cls):
        i = input('Digite o ID do contato: ')
        for c in cls.__contatos:
            if c.get_id() == i:
                ind = cls.__contatos.index(c)
                id = int(input('Digite o novo ID: '))
                no = input('Digite o novo nome: ')
                e = input('Digite o novo email: ')
                f = input('Digite o novo telefone: ')
                na = input('Digite a nova data de nascimento: ')
                x = Contato(id, no, e, f, na)
                cls.__contatos.pop(ind)
                cls.__contatos.insert(ind, x)
    @classmethod
    def excluir(cls):
        i = input('Digite o ID do contato: ')
        for c in cls.__contatos:
            if c.get_id() == i:
                cls.__contatos.remove(c)
    @classmethod
    def pesquisar(cls):
        i = input('Digite as iniciais: ').strip().lower()
        for c in cls.__contatos:
            if c.get_nome().lower().startswith(i):
                print(c)
    @classmethod
    def aniversariantes(cls):
        meses = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
        }
        aniver = []
        i = input('Digite o mês de referência: ')
        try:
            i = int(i)
        except ValueError:
            i = i.lower()
        if type(i) == str:
            i = meses[i]
        for c in cls.__contatos:
            nasc = c.get_nasc()
            if nasc.month == i:
                aniver.append(f'{c.get_nome()}: {nasc.day:02d}/{nasc.month:02d}')
        for a in aniver:
            print(a)
    @classmethod
    def abrir(cls):
        pass
    @classmethod
    def salvar(cls):
        pass