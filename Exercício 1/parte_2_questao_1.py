nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2)/2

if media >= 7 and media < 10:
    print(f"Média final: {media:.2f}. Situação: Aprovado")
elif media < 7:
    print(f"Média final: {media:.2f}. Situação: Reprovado")
elif media == 10:
    print(f"Média final: {media:.2f}. Situação: Aprovado com Distinção")