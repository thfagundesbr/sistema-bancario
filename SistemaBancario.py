deposito_valores = []
saques_valores = []
saldo_conta = 0
valor_depositado = 0
valor_sacado = 0
opcao = 0
QUANTIDADE_SAQUE = 3

def depositar_valores():
    valor_depositado = float(input("Digite o valor a ser depositado: "))
    deposito_valores.append(valor_depositado)
    global saldo_conta
    saldo_conta += valor_depositado
    
def sacar_valores():
    QUANTIDADE_SAQUE = 3
    global saldo_conta
    while QUANTIDADE_SAQUE > 0:
         valor_sacado = float(input("Digite o valor que deseja sacar:"))
         if valor_sacado > 500:
           print("Não é permitido sacar valores acima de 500,00 reais!")
           break
         elif saldo_conta == 0:
             print("Não há saldo disponível.")
             break
         else:
             print(f"Saque do valor {valor_sacado} realizado com sucesso")
             saques_valores.append(valor_sacado)
             saldo_conta -= valor_sacado
             QUANTIDADE_SAQUE -= 1
         
         if QUANTIDADE_SAQUE == 0:
              print("Você atingiu o número máximo de saques diários. Tente novamente amanhã")
            
    


def extrato_conta():
    if saldo_conta == 0:
        print ("Não há movimentações na conta.")
    else:
        print("Valores depositados: ")
        for depositados in deposito_valores:
            print(depositados)
        print("Valores sacados: ")
        for sacados in saques_valores:
            print(sacados)
        print()
        print("SALDO DA CONTA:")
        print(saldo_conta)


print("BANCO FGTHOMAS")
print()
print()
while True:
    QUANTIDADE_SAQUE = 3
    print("[1] Deposito [2] Saque [3] Extrato [4] Sair")
    print()
    print()
    print("Digite o serviço que deseja acessar: ")
    opcao = int(input())
    if opcao == 1:
        depositar_valores()
    elif opcao == 2:
        sacar_valores()
            
    elif opcao == 3:
        extrato_conta()    
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Tente novamente")

print("Obrigado por utilizar o FGTHOMAS!")