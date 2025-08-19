def soma_numeros(numero):
    soma = 0
    for i in range (1,numero+1):
        soma += i
    return soma

numero = int(input("Digite um número: "))
print(soma_numeros(numero))