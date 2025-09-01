'''
13. Defina a função pertenceQ que recebe como argumentos uma 
lista de números inteiros w e um número inteiro  n
e devolve True se  n ocorre em  w e False em caso contrário.
'''

def pertenceQ(lista, num):
    if len(lista) == 0:
        return False
    else:
        return (lista[-1] == num) or pertenceQ(lista[:-1],num)
    
print(pertenceQ([2,3,5,1],1))