lado_a = float(input("Digite o valor do lado A do triângulo: "))
lado_b = float(input("Digite o valor do lado B do triângulo: "))
lado_c = float(input("Digite o valor do lado C do triângulo: "))

if (lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_c + lado_b > lado_a):
    print("Estes lados formam um triângulo!")
    if (lado_a == lado_b and lado_b == lado_c):
        print("É um triângulo equilátero")
    elif (lado_a != lado_b and lado_b != lado_c and lado_a != lado_c):
        print("É um triângulo escaleno")
    else:
        print("É um triângulo isóceles")
else:
    print("Estes lados não formam um triângulo!")