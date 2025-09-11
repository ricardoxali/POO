from datetime import date
class Paciente:
    def __init__(self, n, c, f, dn):
        self.__nome = n
        self.__cpf = c
        self.__fone = f
        na, nm, nd = dn.split('/')
        self.__nasc = date(na, nm, nd)
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    def Idade(self):
        hj = date.today()
        a, m, d = hj.year, hj.month, hj.day
        
