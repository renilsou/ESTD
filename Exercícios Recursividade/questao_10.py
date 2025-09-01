'''
10. Defina a função prod_lista que recebe como argumento 
uma lista de inteiros e devolve o produto dos seus elementos.
'''

def prod_lista(lista):
    if len(lista) == 0:
        return 1
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[-1] * prod_lista(lista[:-1])
    
print(prod_lista([1,2,3,4,5,6]))