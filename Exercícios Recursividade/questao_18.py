'''
19. Defina a função conta que recebe como argumentos uma 
lista de números inteiros  w e um número inteiro  k
e devolve o número de vezes que  k ocorre em  w
'''

def conta(lista, num):
    if len(lista) == 0:
        return 0
    else:
        return (1 if lista[0] == num else 0) + conta(lista[1:],num)
    
print(conta([1,2,3,2,1,2],2))