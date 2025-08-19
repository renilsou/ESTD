def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(compare(a,b))