menu ="""
Escolha a Operação :
[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair
=>""" 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        d = float(input("Informe o valor que deseja depositar:\n R$ "))
        if d>0:
            saldo = saldo + d
            d = f"+ R$ {saldo:.2f}\n"
            extrato = extrato + d
        else:
            print("Informe um Valor valido para Deposito")

    elif opcao == "s":
        print("Saque")
        if numero_saques<LIMITE_SAQUES:    
            a = float(input("Informe o valor que deseja Sacar:\n R$ "))
            if a <=500 and a>0 and a<saldo:
                saldo = saldo - a
                numero_saques +=1
                a = f"- R$ {a:.2f}\n"
                extrato = extrato + a
            else:
                print("Informe um Valor válido para saque")
        else:
            print("Limite de saques atingido")

    elif opcao == "e":
        print("Extrato\n")
        print(extrato)
        print("Saldo\n")
        print(saldo)

    elif opcao == "q":
        print("Obrigado por escolher o  nosso banco")
        break
    else:
        print ("Digite uma opção valida")