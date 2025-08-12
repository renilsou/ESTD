x = int(input("Digite o valor de x: "))

if (x % 2 == 0):
    x = x/2
else:
    x = 3 * x + 1

print(f"Novo valor de x: {x}")