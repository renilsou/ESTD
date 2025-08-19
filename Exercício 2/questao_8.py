import math

def hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1*cateto1) + (cateto2*cateto2)
    hipotenusa = math.sqrt(hipotenusa)
    print(f"Hipotenusa: {hipotenusa}")

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))
hipotenusa(cateto1, cateto2)