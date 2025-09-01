'''
15. Defina a função indices_impar que recebe como 
argumento uma lista de números inteiros  w
e devolve a lista dos elementos de  w
em posições de índice ímpar. Recorde que a primeira posição 
de uma lista tem índice 0, que é um número par.
'''

def indices_impar(lista):
    if len(lista) <= 1:
        return []
    else:
        return [lista[1]] + indices_impar(lista[2:])
    
print(indices_impar([0,1,2,3,4,5,6]))