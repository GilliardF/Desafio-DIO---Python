'''
Baseado na utlima versão do sistema bancario, vamos criar uma nova versão com as seguintes
funcionalidades:

** Regras de negocio
1 - Criar usuário (cliente do banco)
2 - Criar conta para o usuário (Vincular o usuário a conta)
'''

from datetime import datetime


AGENCIA = '0001'
PRIMEIRO_ACESSO =  True # Variavel para verificar se é o primeiro acesso do cliente
EXTRATO = list()
SALDO = float(0)
ID_SAQUE = int(0)
CONTA_BANCARIA = list()
VERIFICADOR_MENU = int()


def criar_conta():
    '''Função para criar a conta e usuário'''
    global PRIMEIRO_ACESSO, CONTA_BANCARIA

    print('*' * 50)
    print(('Cadastro de usuário e conta corrente').center(50))
    print('*' * 50)

    usuario = input('\nDigite o nome do usuário: ')
    conta = input('Digite o número da conta: ')
    agencia = '0001'
    CONTA_BANCARIA.insert(len(CONTA_BANCARIA), [usuario, agencia, conta])

    if PRIMEIRO_ACESSO:
        PRIMEIRO_ACESSO = False

        print(f'\n\nUsuário: {usuario} | Agência: {agencia} | Conta: {conta}')
        print('Cadastro concluído com sucesso!\n')
        print('-' * 50)

    else:
        print(f'\n\nUsuário: {usuario} | Agência: {agencia} | Conta: {conta}')
        print('Cadastro concluído com sucesso!\n')
        print(f'{"-" * 50}\n')
        retorno_menu()

    menu()


def verificador_conta():
    '''Função para verificar se a conta do cliente existe'''
    global CONTA_BANCARIA, EXTRATO, SALDO, LIMITE_SAQUE, VERIFICADOR_MENU

    print('*' * 50)
    print(('Verificação de conta').center(50))
    print('*' * 50)

    verificador_user = input('\nDigite o nome do usuário: ')
    verificador_banco = input('Digite o número da conta bancária: ')

    encontrado = False

    for i, conta in enumerate(CONTA_BANCARIA):
        if verificador_user == conta[0] and verificador_banco == conta[2]:
            encontrado = True
            print('\nUsuário e conta verificados com sucesso!\n')
            print('-' * 50)

            try:
                if VERIFICADOR_MENU == 1:
                    saque(i, CONTA_BANCARIA, EXTRATO)

                elif VERIFICADOR_MENU == 2:
                    deposito(i, CONTA_BANCARIA)

                elif VERIFICADOR_MENU == 3:
                    exibir_extrato(i, CONTA_BANCARIA, EXTRATO)

            except ValueError:
                print('Por favor escolha uma opção válida!')
                print('Utilize somente digitos numéricos!')
                print('Por motivos de segurança essa sessão será encerrada.\n')
                break

    if not encontrado:
        print('\nUsuário e conta inválidos!\nTente novamente, ou crie uma conta.')
        print('Por motivos de segurança essa sessão será encerrada.\n')
        print('-' * 50)

    retorno_menu()


def saque(id_conta, CONTA_BANCARIA, EXTRATO):
    """Função para realizar saque, com as seguintes regras de negocio:"""
    global ID_SAQUE, SALDO

    print('*' * 50)
    print(('Saque').center(50))
    print('*' * 50)

    valor_saque = float(
    input('\nDigite o valor a ser retirado,\nou se preferir digite 0 pera sair: '))

    try:
        if ID_SAQUE < 3 and valor_saque <= 500.00 and valor_saque <= SALDO:
            ID_SAQUE += 1
            SALDO -= valor_saque
            EXTRATO.append(
        [
            f'Saque: R$ {valor_saque:.2f} | Saldo R$: {SALDO:.2f}\n'
            f'\nData: {datetime.now().strftime("%d-%m-%Y")}'
            f' | Hora: {datetime.now().strftime("%H:%M")}'
        ]
)
            print(f'\nValor retirado R$: {valor_saque:.2f}, Saldo R$:{SALDO:.2f}')
            print('\nAção concluída com sucesso!\n')
            print('-' * 50)

        elif ID_SAQUE == 3:
            print('\nLimite de saques diários atingido!')
            print('Por motivos de segurança essa sessão será encerrada.\n')
            print(f'{"-" * 50}\n')

    except ValueError:
        print('Por favor digite um valor válido!')
        print('Utilize somente digitos numéricos!')
        print('Por motivos de segurança essa sessão será encerrada.\n')

    finally:
        if valor_saque > 500.00:
            print('\nValor acima do limite permitido!')
            print('Por favor digite um valor até R$: 500,00')
            print('Por motivos de segurança essa sessão será encerrada.\n')
            print(f'{"-" * 50}\n')

        elif valor_saque > SALDO:
            print('\nSaldo insuficiente!')
            print('Por favor digite um valor menor ou igual ao seu saldo.')
            print('Por motivos de segurança essa sessão será encerrada.\n')
            print(f'{"-" * 50}\n')

        elif valor_saque <= 0:
            if valor_saque == 0:
                print('Obrigado, volte sempre!')
                print('-' * 50)
                exit()

            else:
                print('Digite um valor maior que R$:0,00 para realizar o saque!')
                print('Por motivos de segurança essa sessão será encerrada.\n')
                print(f'{"-" * 50}\n')

    retorno_menu()



def deposito(id_conta, CONTA_BANCARIA):
    '''Função para realizar deposito na conta do cliente'''
    global SALDO, EXTRATO

    print('*' * 50)
    print(('Deposito').center(50))
    print('*' * 50)
    valor_deposito = float(input('\nDigite o valor a ser depositado R$: '))

    try:
        SALDO += valor_deposito
        if valor_deposito > 0:
            EXTRATO.append(
    [
        f'Deposito: R$ {valor_deposito:.2f} | Saldo R$: {SALDO:.2f}\n'
        f'\nData: {datetime.now().strftime("%d-%m-%Y")}'
        f' | Hora: {datetime.now().strftime("%H:%M")}'
    ]
)

            print(f'\nValor depositado R$: {valor_deposito:.2f}, Saldo R$: {SALDO:.2f}\n')
            print('Ação concluída com sucesso!\n')
            print('-' * 50)

    except ValueError:
        if valor_deposito < 0:
            print('Digite um valor maior que 0 para realizar o deposito!')

        else:
            print('Por favor digite um valor válido!')
            print('Utilize somente digitos numéricos!')
            print('Por motivos de segurança essa sessão será encerrada.\n')

    finally:
        retorno_menu()


def exibir_extrato(id_conta, CONTA_BANCARIA, EXTRATO):
    '''Função para exibir o extrato da conta do cliente'''

    conta_extrato = CONTA_BANCARIA[id_conta]

    print(f'{"*" * 16} EXTRATO COMPLETO {"*" * 16}\n')
    print(
        f'Usuário: {conta_extrato[0]} | Agência: {conta_extrato[1]} | Conta: {conta_extrato[2]}\n'
    )
    print(f'{"-" * 50}\n')

    # [for i in EXTRATO for j in i print(j, end=' ')]
    for lista_interna in EXTRATO:
        for elemento in lista_interna:
            print(elemento, end=' ')
        print(f'\n{"=" * 50}\n')
    print('-' * 50)

    retorno_menu()


def retorno_menu():
    '''Função para retornar ao menu principal'''
    global PRIMEIRO_ACESSO

    try:
        verificador_retorno = int(input(
        '\nDeseja realizar outra operação? \n[1] Sim | [2] Não\nDigite aqui: '))

        print()
        print('-' * 50)

        if verificador_retorno == 1:
            menu()

        elif verificador_retorno == 2:
            print()
            print('-' * 50)
            print('Obrigado, volte sempre!')
            print(CONTA_BANCARIA)
            print(PRIMEIRO_ACESSO)
            type(SALDO)
            print('-' * 50)
            exit()

    except ValueError:
        print('-' * 50)
        print('\nPor favor escolha uma opção válida!')
        print('Utilize somente digitos numéricos!')
        print('Tente novamente.\n')
        print('-' * 50)
        retorno_menu()


def primeiro_cadastro():
    '''Função para exibir o menu principal'''

    print('*' * 50)
    print(('Bem vindo ao Banco Digital').center(50))
    print('*' * 50)

    print('\nPor favor, crie usuário e conta.\n')
    print('-' * 50)

    criar_conta()

def menu():
    '''Função para exibir o menu principal'''
    global PRIMEIRO_ACESSO, VERIFICADOR_MENU

    if PRIMEIRO_ACESSO:
        primeiro_cadastro()

    elif not PRIMEIRO_ACESSO:
        print('*' * 50)
        print('Menu Principal'.center(50))
        print('*' * 50)
        print('\nSelecione uma das opções abaixo:\n')
        print('[1] - Saque')
        print('[2] - Deposito')
        print('[3] - Extrato')
        print('[4] - Criar conta')
        print('[0] - Sair')
        print('Observação: Apenas digitos numéricos!\n')
        print('-' * 50)

        try:
            VERIFICADOR_MENU = int(input('Digite aqui: '))
            print('-' * 50)
            if VERIFICADOR_MENU == 0:
                print('Obrigado, volte sempre!')
                exit()

            elif VERIFICADOR_MENU == 4:
                criar_conta()

            verificador_conta()

        except ValueError:
            print('\nPor favor escolha uma opção válida!')
            print('Utilize somente digitos numéricos!')
            print('Por motivos de segurança essa sessão será encerrada.\n')
            print('-' * 50)
            retorno_menu()


print('-' * 50)

menu()
