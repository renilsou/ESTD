def inverter_lista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])

print(inverter_lista(["a","b",1,5,"c"]))