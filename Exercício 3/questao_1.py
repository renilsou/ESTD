palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print(f"A palavra {palavra} é palíndroma")
else:
    print(f"A palavra {palavra} não é palíndroma")