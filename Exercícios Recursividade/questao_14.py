'''
14. Defina a função negpos que recebe como argumento uma 
lista de números inteiros  w e devolve a diferença entre 
o número de números positivos e o número de números 
negativos de w.

return (1 if palavra[0] == letra else 0) 
+ contar_letra(palavra[1:],letra)
'''

def negpos(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return 1 if lista[0] > 0 else -1
    else:
        return (1 if lista[0] > 0 else -1) + negpos(lista[1:])
    
print(negpos([-1,-2,-3,4]))