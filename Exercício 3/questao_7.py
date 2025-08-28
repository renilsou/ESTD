nome = input("Digite seu nome: ")

def gerar_login(nome):
    login = []
    login.append(nome[0])
    for i in range(len(nome)):
        if nome[i] == " ":
            login.append(nome[i+1])
    return "".join(login)

print(f"Login: {gerar_login(nome)}")