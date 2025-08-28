nome = input("Digite o nome completo: ")

def separar_nome(nome):
    nomes_separados = []
    inicias = []
    index = 0
    for i in range(len(nome)):
        if nome[i] == " ":
            nomes_separados.append(nome[index:i])
            index = i+1
    for nome in nomes_separados:
        inicias.append(nome[0])
    return ". ".join(inicias)

def ultimo_nome(nome):
    for i in range(len(nome)):
        if nome[-i] == " ":
            index = i-1
            break
    return nome[-index:]
    
print(f"{ultimo_nome(nome)}, {separar_nome(nome)}")