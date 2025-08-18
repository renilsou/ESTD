def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Digite um número inteiro: "))
print(eh_par(numero))