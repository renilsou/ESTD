def fat_duplo(numero):
    if numero == 1:
        return 1
    if numero % 2 == 0:
        return "Informe um número impar"
    else:
        return numero * fat_duplo(numero-2)
        
print(fat_duplo(10))