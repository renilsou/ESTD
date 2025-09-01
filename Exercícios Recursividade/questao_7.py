'''
5. Defina a função num_perf que recebe como 
argumento um número inteiro positivo e devolve 
True se esse número for um número perfeito e False 
em caso contrário. Recorde que um número perfeito 
é um número natural que é igual à soma de todos 
os seus divisores próprios, isto é, a soma de 
todos os divisores excluindo o próprio número. 
Pode, se assim o entender, definir funções auxiliares.
'''

def divisores(num):
    if num == 0:
        return 0
    else:
        return (num if num % num-1 == 0 else 0) + divisores(num-1)