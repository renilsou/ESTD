frase = input("Digite uma frase: ")
palavra = input("Digite a palavra que deseja substituir: ")
nova_palavra = input("Digite a nova palavra: ")

def separar_frase(frase):
    frase_separada = []
    index = 0
    for i in range(len(frase)):
        if frase[i] == " ":
            frase_separada.append(frase[index:i])
            index = i+1
    for i in range(len(frase)):
        if frase[-i] == " ":
            frase_separada.append(frase[-(i-1):])
            break
    return frase_separada

def substituir_palavra(frase, palavra, nova_palavra):
    for i in range(len(separar_frase(frase))):
        if separar_frase(frase)[i] == palavra:
            separar_frase(frase)[i] = nova_palavra
    return " ".join(separar_frase(frase))

print(substituir_palavra(frase, palavra, nova_palavra))