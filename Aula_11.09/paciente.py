from datetime import date
class Paciente:
    def __init__(self, n, c, f, dn):
        self.__nome = n
        self.__cpf = c
        self.__fone = f
        d, m, a = map(int, dn.split('/'))
        self.__nasc = date(a, m, d)
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    def Idade(self):
        hj = date.today()
        idadeano = hj.year - self.__nasc.year
        idademes = hj.month - self.__nasc.month
        idadedia = hj.day - self.__nasc.day
        a = 'anos'
        m = 'meses'
        if idadedia < 0:
            idademes -= 1
        if idademes < 0:
            idadeano -= 1
            idademes += 12
        if idadeano == 1:
            a = 'ano'
        if idademes == 1:
            m = 'mês'
        return f"Idade: {idadeano} {a} e {idademes} {m}"
    def __str__(self):
        return f"Nome: {self.__nome} - CPF: {self.__cpf} - Telefone: {self.__fone} - Nascimento: {self.__nasc.day}/{self.__nasc.month}/{self.__nasc.year} - {self.Idade()}"