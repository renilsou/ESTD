'''
4. Defina a função media_digitos que recebe 
como argumento um número natural e devolve a 
média dos seus digitos.'''

def soma_digitos(num):
    if num < 10:
        return num
    else:
        return num % 10 + soma_digitos(num // 10)
    
def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)
    
def media_digitos(num):
    return soma_digitos(num) / contar_digitos(num)
    
print(media_digitos(1234))