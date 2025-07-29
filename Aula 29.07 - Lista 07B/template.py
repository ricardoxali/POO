from view import View
from datetime import date
class UI:
    @staticmethod
    def menu():
        op = int(input('1-Inserir, 2-Listar, 3-Listar Específico, 4-Atualizar, 5-Excluir, 6-Pesquisar, 7-Aniversariantes, 8-Sair\n'))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 8:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.listar_id()
            if op == 4: UI.atualizar()
            if op == 5: UI.excluir()
            if op == 6: UI.pesquisar()
            if op == 7: UI.aniversariantes()
    @staticmethod
    def inserir():
        i = int(input('Digite o ID: '))
        no = input('Digite o nome: ')
        e = input('Digite o e-mail: ')
        f = input('Digite o telefone: ')
        d, m, a = map(int, input('Digite a data de nascimento: ').split('/'))
        View.contato_inserir(i, no, e, f, date(a, m, d))
        print('Contato inserido com sucesso')
    @staticmethod
    def listar():
        for c in View.contato_listar():
            print(c)
    @staticmethod
    def listar_id():
        i = int(input('Digite o ID: '))
        print(View.contato_listar_id(i))
    @staticmethod
    def atualizar():
        i = int(input('Digite o ID atual: '))
        id = int(input('Digite o novo ID: '))
        no = input('Digite o novo nome: ')
        e = input('Digite o novo email: ')
        f = input('Digite o novo telefone: ')
        d, m, a = map(int, input('Digite a nova data de nascimento: ').split('/'))
        View.contato_atualizar(i, id, no, e, f, date(a, m, d))
        print('Contato atualizado com sucesso')
    @staticmethod
    def excluir():
        i = int(input('Digite o ID: '))
        View.contato_excluir(i)
        print('Contato exluído com sucesso')
    @staticmethod
    def pesquisar():
        i = input('Digite as iniciais: ').strip().lower()
        for c in View.contato_pesquisar(i):
            print(c)
    @staticmethod
    def aniversariantes():
        i = input('Digite o mês de referência: ')
        for c in View.contato_aniversariantes(i):
            print(c)

UI.main()