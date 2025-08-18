soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1} número: "))
    soma += numero

print(f"Média dos números digitados: {(soma/5):.2f}")