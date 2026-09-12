opção = int(input("Digite uma opção: "))
match opção: 
    case 1:
        print("Consutar saldo")
    case 2: 
        print("Fazer depósito")
    case 3: 
        print("Fazer saque")
    case 4: 
        print("Sair")
    case _:
        print("Opção inválida")