while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota <= 10 and nota >= 0:
        print("Nota válida!")
        break
    else:
        print("Valor inválido!")
    