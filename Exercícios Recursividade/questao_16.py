'''
16. Defina a função escolhe_pares que recebe como 
argumento uma lista de números inteiros  w
e devolve a lista dos elementos pares de  w.
'''

def escolhe_pares(lista):
    if len(lista) == 0:
        return []
    else:
        return ([lista[0]] if lista[0] % 2 == 0 else []) + escolhe_pares(lista[1:])
    
print(escolhe_pares([1,2,3,4,4,2,6,8,9]))