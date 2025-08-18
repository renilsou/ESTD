anos = 0

pais_A = 80000
pais_B = 200000

while True:
    if pais_A < pais_B:
        pais_A += pais_A*0.03
        pais_B += pais_B*0.015
        anos += 1
    else:
        print(f"População de A: {pais_A:.2f}\nPopulação de B {pais_B:.2f}\nAnos decorridos: {anos}")
        break