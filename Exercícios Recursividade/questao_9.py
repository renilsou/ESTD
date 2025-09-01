'''
9. Defina a função quadrados_inv que recebe como argumento 
um número natural  n e devolve a lista dos quadrados 
perfeitos até  n, por ordem decrescente.
'''

def quadrados_inv(num):
    if num == 1:
        return print(1)
    else:
        print(num**2)
        return quadrados_inv(num-1)
    
quadrados_inv(6)