class Agua:
    def __init__(self):    # Encapsulamento
        self.__mes = 1
        self.__ano = 2025
        self.__consumo = 0
    def set_mes(self, v):  # método de acesso: set para ajustar o valor do atributo
        if v < 1 or v > 12: raise ValueError("O mês deve estar entre 1 e 12")   # validação
        self.__mes = v  
    def set_ano(self, v):
        if v == 0: raise ValueError("O ano não pode ser zero")                  # validação
        self.__ano = v
    def set_consumo(self, v):
        if v < 0: raise ValueError("O consumo não pode ser negativo")           # validação
        self.__consumo = v   
    def get_mes(self):     # método de acesso: get para retornar o valor do atributo
        return self.__mes           
    def get_ano(self):
        return self.__ano           
    def get_consumo(self):
        return self.__consumo           
    def valor(self):
        if self.__consumo <= 10: return 38
        if 11 <= self.__consumo <= 20: return 38 + (self.__consumo - 10) * 5
        if self.__consumo > 20: return 38 + 50 + (self.__consumo - 20) * 6  

class Triangulo:
    def __init__(self):
        self.__base = 1
        self.__altura = 1
    def set_base(self, v):
        if v < 1: raise ValueError('A base deve ser maior que 0')
        self.__base = v
    def set_altura(self, v):
        if v < 1: raise ValueError('A altura deve ser maior que 0')
        self.__altura = v
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def area(self):
        return self.__base * self.__altura / 2

class UI: # UI = User Interface: print e input
    @staticmethod
    def menu():
        op = int(input("Informe uma opção: 1-Conta d'água, 2-Triângulo, 9-Fim: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = UI.menu()
           if op == 1: UI.agua()
           if op == 2: UI.triangulo()
    @staticmethod
    def agua():
        x = Agua()
        x.set_mes(int(input("Informe o mês da conta: ")))
        x.set_ano(int(input("informe o ano: ")))
        x.set_consumo(int(input("informe o consumo em m3: ")))
        print(f"O valor da conta de água do mês {x.get_mes()} do ano {x.get_ano()} é {x.valor()}")
    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(int(input("Informe o valor da base: ")))
        x.set_altura(int(input("Informe o valor da altura: ")))
        print(f"O triângulo de base {x.get_base()} e altura {x.get_altura()} tem área {x.area()}")

UI.main()