from datetime import date
from utils.helper import date_para_str, str_para_date

class Cliente:
    
    contador = 101
    
    def __init__(self, nome, email, cpf, data_nascimento) -> None:
        self.__codigo = Cliente.contador
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento = str_para_date(data_nascimento)
        self.__data_cadatro = date.today()
        Cliente.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def data_nascimento(self) -> str:
        return date_para_str(self.__data_nascimento)
    
    @property
    def data_cadastro(self) -> str:
        return date_para_str(self.__data_cadatro)
    
    def __str__(self) -> str:
        return f'Código: {self.codigo}\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nData de Cadastro: {self.data_cadastro}'