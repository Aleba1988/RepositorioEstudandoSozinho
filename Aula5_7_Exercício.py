for aluno in range(5):
    nota = float(input("Digite a nota: "))
    
    if nota >= 7:
        print("Aprovado")
    elif 5<= nota <= 6.99:
        print("Recuperação")
    else:    
        print("Reprovado")  