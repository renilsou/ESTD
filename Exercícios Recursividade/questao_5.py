'''
3. Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n
 .
'''

def prim_alg(num):
    if num < 10:
        return num
    else:
        return prim_alg(num//10)
    
print(prim_alg(5629))