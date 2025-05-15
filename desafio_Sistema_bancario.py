menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0

# Funções
def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        return saldo
    else:
        print("Valor inválido para depósito.")
        return saldo

def sacar(saldo, valor, limite):    
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor acima do limite de saque.")
    else:
        saldo -= valor
        return saldo
    return saldo


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            depositar(saldo, valor)
            saldo += valor
            extrato += f"Depósito: R$ {saldo:.2f}\n"
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        if numero_saques == 3:
            print("Limite de saques diários atingido.")
        else:
            sacar(saldo, valor, limite)
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"


    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")
