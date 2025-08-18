def eh_primo(numero):
    contador = 0
    for i in range(2, numero+1):
        if numero % i == 0:
            contador += 1
    if numero == 2:
        return True
    else:
        if contador == 0:
            return True
        else:
            return False
        
numero = int(input("Digite um número: "))
print(eh_primo(numero))