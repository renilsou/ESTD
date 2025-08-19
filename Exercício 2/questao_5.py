def maior_de_2(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "Iguais"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(maior_de_2(num1,num2))