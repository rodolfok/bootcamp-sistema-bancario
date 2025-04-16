menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valorDeposito = float(input("Valor do depósito: "))
        if valorDeposito > 0:
            saldo = saldo + valorDeposito
            extrato += f"Depósitou Valor: R$ {valorDeposito:.2f}\n"
        else:
            print("Não foi possivel fazer o deposito")

    elif opcao == "s":
        valorSaque = float(input("Valor do saque: "))
        
        if valorSaque > saldo:
            print("Saldo insuficiente. Tente outro valor")
            print(f"\n Seu Saldo: R$ {saldo:.2f}")

        elif valorSaque > limite:
            print("Saque excede o limite.")
            print(f"\n Limite permitido saque: R$ {limite:.2f}")

        elif numero_saques >= LIMITE_SAQUES:
            print("Quantidade máxima de saques excedido.")

        elif valorSaque > 0:
            saldo -= valorSaque
            extrato += f"Sacou Valor: R$ {valorSaque:.2f}\n"
            numero_saques += 1
            print(f"\n Seu Saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("\n###### EXTRATO ######")
        print("Não foram realizadas \nmovimentações bancárias." if not extrato else extrato)
        print(f"\nSaldo na Conta: R$ {saldo:.2f}")
        print("######################")

    elif opcao == "q":
        break

    else:
        print("Selecione novamente a operação desejada.")