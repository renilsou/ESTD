altura = int(input("Digite a altura em centímetros: "))
peso_ideal_homem = (72.7 * (altura/100)) - 58
peso_ideal_mulher = (62.1 * (altura/100)) - 44.7

print(f"Peso ideal para uma pessoa com {(altura/100):.2f} m de altura:\nSe for homem: {peso_ideal_homem:.2f}\nSe for mulher: {peso_ideal_mulher:.2f}")