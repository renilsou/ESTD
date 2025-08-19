def fatorial (numero):
    fatorial = numero
    for i in range(1,numero):
        fatorial *= i
    print(f"Fatorial de {numero}: {fatorial}")

numero = int(input("Digite um número: "))
fatorial(numero)