'''
1. Defina a função soma_nat que recebe como argumento um número natural  n
e devolve a soma de todos os números naturais até  n
'''

def soma_nat(num):
    if num == 0:
        return 0
    else:
        return num + soma_nat(num-1)
    
print(soma_nat(5))