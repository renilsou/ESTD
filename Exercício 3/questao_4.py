nome = input("Digite nome completo: ")

def ultimo_nome(nome):
    for i in range(len(nome)):
        if nome[-i] == " ":
            index = i-1
            break
    return nome[-index:]

def primeiro_nome(nome):
    for i in range(len(nome)):
        if nome[i] == " ":
            index = i
            break
    return nome[:index]

print(f"{ultimo_nome(nome)}/{primeiro_nome(nome)}")