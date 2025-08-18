maior = 0
menor = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1} número: "))
    
    if (i == 0):
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"Maior número: {maior}\nMenor número: {menor}")