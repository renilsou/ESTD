def dia_da_semana(dia):
    if dia == 1:
        return"Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "Inválido: número não corresponde a nenhum dia da semana"
    
dia = int(input("Digite um número correspondente a um dia da semana: "))
print(dia_da_semana(dia))