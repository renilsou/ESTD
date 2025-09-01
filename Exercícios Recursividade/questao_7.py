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
def soma_divisores(num, div):
    if div == 0:
        return 0
    elif num % div == 0:
        return div + soma_divisores(num, div-1)
    else:
        return soma_divisores(num, div-1)

def num_perf(num):
    return num == soma_divisores(num, num-1)

print(num_perf(5))