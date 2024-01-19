'''
DESAFIO

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizas 
suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar
apenas 3 operações: depósito, saque e extrato.

* Regras de negócio
Depósitos somente com valores positivos.
Extratos devem ser apresentados conforme exemplo: R$ 1500.45
Limite de 3 saques diários com limite de R$500,00 por saque.
'''

extrato = []
saldo = float(0)
limite_saque = 3
limite_valor_saque = 500.00
id_saque = 0


def saque():
       global extrato
       global saldo
       global id_saque

       
       valor_saque = float(input('Digite o valor a ser retirado,\nou se preferir digite 0 pera sair: '))
       if valor_saque >= 0 and valor_saque > saldo:
              while valor_saque > saldo:
                     if valor_saque > saldo:
                            print('Saldo insuficiente!')

                     elif valor_saque >= 0:
                            print('Digite um valor superior a R$ 0,00.')
                     print('-' * 50)
                     valor_saque = int(input('Digite o valor a ser retirado R$: '))
                     print('-' * 50)
       
              
       elif valor_saque < saldo and id_saque < 3:
              id_saque += 1
              if valor_saque < limite_valor_saque:
                     saldo -= valor_saque
                     extrato.append(['Saque R$:', valor_saque, '| Saldo R$:', saldo])
                     print(f'\nValor retirado R$: {valor_saque}, Saldo R$:{saldo}')
                     print('\nAção concluída com sucesso!\n')
                     print('-' * 50)
              else:
                     print('\nLimite diário de saque é de R$ 500,00.\n')

       
       else:
              print('\nVocê ultrapasou o limite de 3 (três) saques por dia.\n')

       retorno_menu()


def deposito():
       global saldo
       global extrato

       valor_deposito = float(input('Digite o valor a ser depositado R$: '))

       if valor_deposito > 0:
              saldo += valor_deposito
              extrato.append(['Deposito R$:', valor_deposito, '| Saldo RS:', saldo])
              print(f'\nValor depositado R$: {valor_deposito}, Saldo R$: {saldo}\n')
              print('Ação concluída com sucesso!\n')

       else:
              print('Digite um valor maior que 0 para realizar o deposito!')

       retorno_menu()


def func_extrato():
       global extrato

       print(f'{'*' * 16} EXTRATO COMPLETO {'*' * 16}\n')

       for lista_interna in extrato:
              for elemento in lista_interna:
                      print(elemento, end=' ')
              print()
              print('=' * 50)
       print()
       print('-' * 50)
       print()
       
       retorno_menu()


def retorno_menu():

       retorno_menu = int(input('Deseja realizar outra operação? \n[1] Sim | [2] Não\nDigite aqui: '))
       print('-' * 50)

       if retorno_menu == 1:
              menu()
       
       elif retorno_menu == 2:
              exit()

       else:
              print('Por favor escolha uma opção válida!')
              print('Observação: Apenas digitos numéricos!')
              print('Por motivos de segurança será retornado para o menu principal!\n')
              print('-' * 50)
              
       menu()

                 

def menu():
       print('Selecione uma das opções abaixo:\n')
       print('1 - Saque')
       print('2 - Deposito')
       print('3 - Extrato')
       print('0 - Sair')
       print('Observação: Apenas digitos numéricos!\n')
       print('-' * 50)

       verificador = int(input('Digite aqui: '))
       print('-' * 50)
       while verificador != 0:
              if verificador == 1:
                     saque()
              
              elif verificador == 2:
                     deposito()

              elif verificador ==3:
                     func_extrato()

              else:
                     print('Digite uma opção válida:\n')
                     print('1 - Saque')
                     print('2 - Deposito')
                     print('3 - Extrato')
                     print('0 - Sair')
                     print('Observação: Apenas digitos numéricos!\n')

                     verificador = int(input('Digite aqui: '))
                     print('-' * 50)

       if verificador == 0:
              print('Obrigado, volte sempre!')
              exit()

       else:
              menu()

print('-' * 50)
print('\nSeja bem vindo!\n')
menu()

