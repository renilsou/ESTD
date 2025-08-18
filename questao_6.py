def maior_de_3(num1, num2, num3):
    maior = num1
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    elif num3 > num2 and num3 > num1:
        maior = num3
    return maior

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

print(maior_de_3(num1, num2, num3))