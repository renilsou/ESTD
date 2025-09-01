'''
12. Defina a função todos_imparesQ que recebe como argumento 
uma lista de números inteiros  we devolve True se  w
contém apenas números ímpares e False em caso contrário.
'''
def eh_impar(num):
    if num % 2 != 0:
        return True
    else:
        return False

def todos_imparesQ(lista):
    if len(lista) == 0:
        return True
    else:
        return eh_impar(lista[-1]) and todos_imparesQ(lista[:-1])
    
print(todos_imparesQ([1,3,5,7]))