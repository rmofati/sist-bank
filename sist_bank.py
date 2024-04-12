"""
    max 3 saques por dia
    se não tiver saldo, informar que Não é possível sacar por falta de saldo
    saques e depositos devem ser armazenados para serem mostradas em operação de extrato
    no fim do extrato devem mostrar o saldo atual da conta
    valores devem ser mostrados como R$xxxx.xx
"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

LIMITE_SAQUES = 3
saldo = 0.0
numero_saques = 0
extrato = ""

while True:
    opcao_escolhida = input(menu)

    if opcao_escolhida == "d":
        valor = float(input("Qual o valor que deseja depositar? "))

        if valor > 0:
            saldo += valor
            print(f"Deposito de R${valor:.2f} efetuado com sucesso!\n")
            print(f"Seu saldo atual é de R${saldo:.2f}")
            extrato += f"Depósito de R${valor:.2f}\n"
        else:
            print("Operação não executada. O valor informado é negativo")

    elif opcao_escolhida == "s":
        print(numero_saques >= LIMITE_SAQUES)
        print("num saques: " + str(numero_saques))
        print("limite saq: " + str(LIMITE_SAQUES))

        if numero_saques >= LIMITE_SAQUES:
            print(f"Não é possível realizar mais saques. O valor limite de {LIMITE_SAQUES} saques foi atingido.")
        else:
            valor = float(input("Qual o valor que deseja sacar? "))

            if valor <= saldo:
                saldo -= valor
                numero_saques += 1
                print(f"Saque de R${valor:.2f} efetuado com sucesso!\n")
                print(f"Seu saldo atual é de R${saldo:.2f}")
                extrato += f"Saque de R${valor:.2f}\n"
                print(f"Num saques: {numero_saques}")
            else:
                print(f"Operação não executada. Não existe saldo suficiente. Seu saldo atual é de: R${saldo:.2f}")

    elif opcao_escolhida == "e":
        print("==================== EXTRATO ====================\n")
        print(extrato)
        print("\n")
        print(f"O seu saldo atual é de R${saldo:.2f}")
        print("================== FIM EXTRATO ==================\n")

    elif opcao_escolhida == "q":
        break

    else:
        print("Opção inválida. Informe uma das opções abaixo:")