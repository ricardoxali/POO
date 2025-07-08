print('Questão 1 - Um Paciente')
from datetime import date
class Paciente:
    def __init__(self, n, c, f, dn):
        self.__nome = n
        self.__cpf = c
        self.__fone = f
        self.__nasc = dn
    def Idade(self):
        dn, mn, an = map(int, self.__nasc.split('-'))
        hoje = date.today()
        self.__idadeano = hoje.year - an
        self.__idademes = hoje.month - mn
        self.__idadedia = hoje.day - dn
        if self.__idadedia < 0:
            self.__idademes -= 1
        if self.__idademes < 0:
            self.__idadeano -= 1
            self.__idademes += 12
        return f'O paciente {self.__nome} tem {self.__idadeano} anos e {self.__idademes} meses'
    def get_cpf(self):
        return self.__cpf
    def __str__(self):
        return f'{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nasc}'
    
class PacienteUI:
    __pacientes = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.calc_idade()
    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Calcular Idade, 6-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        nome = input('Informe o nome do paciente: ')
        cpf = input('Informe o cpf: ')
        fone = input('Informe o número de telefone: ')
        nasc = input('Informe a data de nascimento: ')
        p = Paciente(nome, cpf, fone, nasc)
        cls.__pacientes.append(p)
    @classmethod
    def listar(cls):
        for c in cls.__pacientes:
            print(c)
    @classmethod
    def atualizar(cls):
        c = input('Informe o cpf: ')
        for n in cls.__pacientes:
            if n.get_cpf() == c:
                i = cls.__pacientes.index(n)
                nome = input('Informe o nome do paciente: ')
                cpf = input('Informe o cpf: ')
                fone = input('Informe o número de telefone: ')
                nasc = input('Informe a data de nascimento: ')
                x = Paciente(nome, cpf, fone, nasc)
                cls.__pacientes.pop(i)
                cls.__pacientes.insert(i, x)
    @classmethod
    def excluir(cls):
        c = input('Informe o cpf: ')
        for n in cls.__pacientes:
            if n.get_cpf() == c:
                cls.__pacientes.remove(n)
    @classmethod
    def calc_idade(cls):
        c = input('Informe o cpf: ')
        for n in cls.__pacientes:
            if n.get_cpf() == c:
                print(n.Idade())

print()

print('Questão 2 - Um Boleto')
