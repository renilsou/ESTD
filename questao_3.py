def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

numero = int(input("Digite um número inteiro: "))
par_ou_impar(numero)