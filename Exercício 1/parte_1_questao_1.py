soma_notas = 0

for i in range (4):
    nota = float(input(f"Digite a {i+1} nota: "))
    soma_notas += nota

media = soma_notas/4

print(f"Média das notas: {media}")