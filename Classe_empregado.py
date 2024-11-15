#Ana Eloisa Ferreira, Larissa Silva.

class Empregado:
    def __init__(self, nome: str, cpf: int, salario: float):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    # parte para informar os descontos 
    def calcular_descontos(self):
        if self.__salario > 8000:
            desconto = self.__salario * 0.35
        elif 4000 <= self.__salario <= 8000:
            desconto = self.__salario * 0.30
        else:
            desconto = self.__salario * 0.20
        
        print(f"O valor do desconto é R$ {desconto:.2f}")
        
        # Atualiza o salário
        self.__salario -= desconto
        print(f"O salário com o desconto aplicado é R$ {self.__salario:.2f}")
 
def testar_empregado():
    nome = input("Informe o nome do empregado(a): ")
    cpf = int(input("Insira o CPF do empregado(a): "))
    salario = float(input("Digite o salário do empregado(a): "))

    empregado = Empregado(nome, cpf, salario)
    empregado.calcular_descontos()
    print(f"seu salário com o desconto é R$ {empregado.get_salario():.2f}")

if __name__ == "__main__":
    testar_empregado()
