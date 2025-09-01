'''
17. Defina a função retira_negativos que recebe como 
argumento uma lista de números inteiros  w e devolve a lista 
resultante de retirar todos os números negativos de  w
'''

def retira_negativos(lista):
    if len(lista) == 0:
        return []
    else:
        return ([lista[0]] if lista[0] >= 0 else []) + retira_negativos(lista[1:])
    
print(retira_negativos([1,-2,-3,7,0]))