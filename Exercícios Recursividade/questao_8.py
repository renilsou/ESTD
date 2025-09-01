'''
8. Defina a função quadrados que recebe como argumento um 
número natural  n e devolve a lista dos  n
primeiros quadrados perfeitos.
'''

def quadrado(num):
    if num == 1:
        return print(1)
    else:
        quadrado(num-1)
        return print(num**2)
    
quadrado(6)