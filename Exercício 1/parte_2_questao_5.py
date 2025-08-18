ano = int(input("Digite um número correspondente a um determinado ano: "))


if ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto")
elif ano % 4 == 0 and ano % 100 == 0:
    if ano % 400 == 0:
        print(f"{ano} é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")