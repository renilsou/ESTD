x = int(input("Digite o valor de x: "))

while x != 1:
    if (x % 2 == 0):
        x = x / 2
    else:
        x = 3 * x + 1
    print(int(x), end = " -> ")