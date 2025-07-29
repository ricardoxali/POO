from datetime import date
class Contato:
    def __init__(self):
        self.__id = 1
        self.__nome = 'ricardo'
        self.__email = 'r@gmail.com'
        self.__fone = '45'
        self.__nasc = date(2008, 5, 12)
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.day:02d}/{self.__nasc.month:02d}/{self.__nasc.year}"
    
print(Contato())
