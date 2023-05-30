from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print('***********************************')
    print('************** ATM ****************')
    print('***********************************')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta:')
    print('2 - Efetuar saque:')
    print('3 - Efetuar deposito:')
    print('4 - Efetuar transferência:')
    print('5 - Listar conta:')
    print('6 - Sair:')

    opcao = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        exit(1)
    else: 
        print('Opcao inválida!')
        menu()

def criar_conta() -> None:
    print('informe od dados do cliente:')

    nome = str(input('Nome: '))
    email = str(input('Email: '))
    cpf = str(input('CPF: '))
    data_nascimento = str(input('Data Nascimento: '))

    cliente = Cliente(nome, email, cpf, data_nascimento)
    conta = Conta(cliente)

    contas.append(conta)

    print('-----------------------')
    print(f'Conta criado com sucesso!')
    print(f'Dados:')
    print('-----------------------')
    print(conta)
    print('-----------------------')

    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero = int(input('informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor = float(input('Informe o valor do saque: '))
            conta.sacar(valor)    
        else:
            print(f'Não foi encontrada a conta com númer {numero}')
    else:
        print('Ainda não existe contas cadastradas!')
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        
        numero = int(input('informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        
        if conta:
            valor = float(input('Informe o valor do deposito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas!')
    menu()

def efetuar_transferencia() -> None:
    if len(contas) >= 1 :

        numero_o = int(input('Informe o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)
        
        if conta_o:
            
            numero_d = int(input('Informe o número da conta destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)
            
            if conta_d:
                valor = float(input('Informe o valor para transferencia: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'Conta {numero_d} não existe!')
        
        else:
            print(f'Conta {numero_o} não existe!')

    else:
        print('Contas insulficiente para transferência: ')
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('--------------------------------')
        print('------ Listagem de contas  -----')

        for conta in contas:
            print(conta)       
    else:
        print('Não existe contas cadastradas!')
    menu()

def buscar_conta_por_numero(numero) -> Conta:
    return_conta: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                return_conta = conta
    return return_conta

if __name__ == '__main__':
    main()