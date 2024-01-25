menu = """\n==========Banco Chomp==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
===============================
=> """

saldo = 0
limite_total = 1500  # Limite total
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3
LIMITE_SAQUE_MAXIMO = 500

while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("Depósito:")
        deposito = float(input("Quanto você deseja depositar? "))
        
        if deposito > 0:
            print("Deposito relizado com sucesso!")
            
            saldo += deposito

            extrato += f"Depósito: +R$ {deposito:.2f}\n"

            print(f"Saldo atual: R$ {saldo:.2f} ")

        else:
            print("Operação invalida, coloque o valor novamente")
        

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES_DIARIO:
            print("Sacar:")
            saque = float(input("Quanto você deseja sacar? "))
            
            if saque > 0 and saque <= LIMITE_SAQUE_MAXIMO and saque <= saldo:
                if limite_total - saque >= 0:
                    print("Saque realizado com sucesso!")
                    
                    saldo -= saque
                    extrato += f"Saque: -R$ {saque:.2f}\n"
                    limite_total -= saque
                    
                    numero_saques += 1
                    print(f"Saldo atual: R$ {saldo:.2f}")
                else:
                    print("Limite total de saques atingido. Tente novamente amanhã.")
            else:
                print("Operação inválida. Verifique se o valor do saque é válido.")
        else:
            print("Limite diário de saques atingido. Tente novamente amanhã.")



    elif opcao == "3":
        print("\n==========Extrato==========")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===========================")



    elif opcao == "4":
        print("Obrigado por usar nosso sistema bancario! Novas atualizações em breve.")
        print()
        break
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")