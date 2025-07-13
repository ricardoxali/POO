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

PacienteUI.main()

print()

print('Questão 2 - Um Boleto')
from enum import Enum

class Pagamento(Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2
class Boleto:
    def __init__(self, cb, de, dv, vb):
        self.__codBarras = cb
        self.__dataEmissao = de
        self.__dataVencimento = dv
        self.__dataPago = None
        self.__valorBoleto = vb
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EmAberto
    def Pagar(self, v):
        if v <= 0:
            print("Valor inválido!")
            return
        self.__valorPago += v
        self.__dataPago = date.today()
        self.__situacaoPagamento = self.Situacao()
    def Situacao(self):
        if self.__valorPago == 0:
            return Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            return Pagamento.PagoParcial
        else:
            return Pagamento.Pago
    def __str__(self):
        de, me, ae = self.__dataEmissao.split('/')
        dv, mv, av = self.__dataVencimento.split('/')
        if self.__dataPago:
            dp, mp, ap = self.__dataPago.day, self.__dataPago.month, self.__dataPago.year
            pagamento = f'{dp}/{mp}/{ap}'
        else:
            pagamento = "Não pago"
        return (
            f"\n--- Detalhes do Boleto ---\n"
            f"Código de Barras   : {self.__codBarras}\n"
            f"Data de Emissão    : {de}/{me}/{ae}\n"
            f"Data de Vencimento : {dv}/{mv}/{av}\n"
            f"Data do Pagamento  : {pagamento}\n"
            f"Valor do Boleto    : R$ {self.__valorBoleto:.2f}\n"
            f"Valor Pago         : R$ {self.__valorPago:.2f}\n"
            f"Situação           : {self.__situacaoPagamento.name}\n"
        )

class BoletoUI:
    __boleto = []
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = BoletoUI.menu()
            if op == 1: BoletoUI.registrar()
            if op == 2: BoletoUI.exibir()
            if op == 3: BoletoUI.atualizar()
            if op == 4: BoletoUI.pagar()
    @staticmethod
    def menu():
        print("1-Registrar, 2-Exibir, 3-Atualizar, 4-Pagar, 5-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def registrar(cls):
        cb = input('Informe o código de barras: ')
        de = input('Informe a data de emissão: ')
        dv = input('Informe a data de vencimento: ')
        vb = float(input('Informe o valor do boleto: '))
        b = Boleto(cb, de, dv, vb)
        cls.__boleto.append(b)
    @classmethod
    def exibir(cls):
        for c in cls.__boleto:
            print(c)
    @classmethod
    def atualizar(cls):
        cb = input('Informe o código de barras: ')
        de = input('Informe a data de emissão: ')
        dv = input('Informe a data de vencimento: ')
        vb = float(input('Informe o valor do boleto: '))
        b = Boleto(cb, de, dv, vb)
        cls.__boleto.clear()
        cls.__boleto.append(b)
    @classmethod
    def pagar(cls):
        vp = float(input('Informe o valor pago: '))
        cls.__boleto[0].Pagar(vp)
        print('Pagamento registrado')

BoletoUI.main()

print()

print('Questão 3 - Uma Agenda de Contatos')
class Contato:
    def __init__(self, i, n, e, f, dn):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = dn
    def get_nome(self):
        return self.__nome
    def get_nasc(self):
        return self.__nasc
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc}"
    
class ContatoUI:
    __contatos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversariantes()
    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 7-Fim")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        nasc = input("Informe a data de nascimento: ")
        dia, mes, ano = map(int, nasc.split('/'))
        c = Contato(id, nome, email, fone, date(ano, mes, dia))
        cls.__contatos.append(c)
    @classmethod
    def listar(cls):
        for c in cls.__contatos:
            print(c)
    @classmethod
    def atualizar(cls):
        n = input('Informe o nome: ')
        for c in cls.__contatos:
            if c.get_nome() == n:
                i = cls.__contatos.index(c)
                id = input('Novo id do contato: ')
                nome = input('Novo nome: ')
                email = input('Novo email: ')
                fone = input('Novo telefone: ')
                nasc = input('Nova data de nascimento: ')
                dia, mes, ano = map(int, nasc.split('/'))
                x = Contato(id, nome, email, fone, date(ano, mes, dia))
                cls.__contatos.pop(i)
                cls.__contatos.insert(i, x)
    @classmethod
    def excluir(cls):
        n = input('Informe o nome: ')
        for c in cls.__contatos:
            if c.get_nome() == n:
                cls.__contatos.remove(c)
    @classmethod
    def pesquisar(cls):
        n = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(n): print(c)
    @classmethod
    def aniversariantes(cls):
        aniver = []
        m = input('Informe o mês de referência: ')
        meses = {
            'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4,
            'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
            'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
        }
        try:
            mes = int(m)
            if mes < 1 or mes > 12: 
                print('Mês inválido')
                return
        except ValueError:
            mes = meses.get(m.lower(), 0)
            if mes == 0:
                print('Mês inválido')
                return
        for c in cls.__contatos:
            if c.get_nasc().month == mes:
                aniver.append(c)
        if len(aniver) == 0:
            print('Nenhum aniversariante')
        else:
            for c in aniver:
                aniversario = c.get_nasc().strftime('%d/%m/%Y')
                print(f'{c.get_nome()}: {aniversario}')

ContatoUI.main()