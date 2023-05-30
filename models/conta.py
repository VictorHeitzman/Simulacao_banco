from models.cliente import Cliente
from utils.helper import formata_float_str

class Conta:

    codigo = 1001

    def __init__(self, cliente: Cliente) -> None:
        self.__numero = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100
        self.__saldo_total = self.calcula_saldo_total
        Conta.codigo += 1

    def __str__(self) -> str:
        return f'Número: {self.numero}\nCliente: {self.__cliente.nome}\nSaldo Total: {formata_float_str(self.__saldo_total)}' 
    
    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def cliente(self) -> str:
        return self.__cliente
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @saldo.setter
    def set_saldo(self, valor) -> None:
        self.__saldo = valor
    
    @property
    def limite(self) -> float:
        return self.__limite
    
    @limite.setter
    def set_limite(self, valor) -> None:
        self.__limite = valor
    
    @property
    def saldo_total(self) -> float:
        return self.__saldo_total
    
    @saldo_total.setter
    def set_saldo_total(self, valor) -> None:
        self.__saldo_total = valor

    @property
    def calcula_saldo_total(self) -> float:
        return self.saldo + self.limite 
    
    def depositar(self, valor) -> None:
        if valor > 0:
            self.set_saldo = self.saldo + valor
            self.set_saldo_total = self.calcula_saldo_total
            print('Deposito efetuado com sucesso!')
        else:
            return print('Informe um valor positivo')
            
    
    def sacar(self, valor) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.set_saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
            else:
                restante = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
                print('Saque efetuado com sucesso!')
        else:
            print('Valor de saque insuficiente') 

    def transferir(self, destino: object, valor) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.set_saldo = self.saldo - valor
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante = self.saldo - valor
                self.saldo = 0
                self.set_limite = self.limite + restante
                self.saldo_total = self.calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.calcua_saldo_total
            print('transferencia efetuado com sucesso!')                 
        else:
            print('valor insuficiente para tranferir!')