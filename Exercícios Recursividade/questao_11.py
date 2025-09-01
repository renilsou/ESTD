'''
11. Defina a função contem_parQ que recebe como argumento 
uma lista de números inteiros w e devolve True se w
contém um número par e False em caso contrário.
'''
def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

def contem_parQ(lista):
    if len(lista) == 0:
        return False
    else:
        return eh_par(lista[-1]) or contem_parQ(lista[:-1])
    
print(contem_parQ([1,3,5,7,9,10]))