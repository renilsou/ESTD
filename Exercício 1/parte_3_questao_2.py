while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == nome_usuario:
        print("Erro: a senha não pode ser igual ao nome de usuário!")
    else:
        print("Nome e senha validados!")
        break
