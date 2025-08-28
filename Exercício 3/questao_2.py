texto = input("Digite um texto: ")

def texto_vazio(texto):
    contador = 0
    for i in range (len(texto)):
        if texto[i] != " ":
            contador =+ 1
    if contador == 0:
        return True
    else:
        return False

def contar_palavras(texto):
    if texto_vazio(texto) == True:
        return 0
    else:
        texto_separado = []
        index = 0
        for i in range(len(texto)):
            if texto[i] == " ":
                texto_separado.append(texto[index:i])
                index = i+1
        return len(texto_separado)+1
    
print(f"Quantidade de palavras: {contar_palavras(texto)}")