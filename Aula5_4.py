for aluno in range(1, 1001):
    nota = float(input("Digite a nota: "))

    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:       
        print("Reprovado")  