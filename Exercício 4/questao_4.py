def crescente(numero):
    if numero == 0:
        print(numero)
    else:
        crescente(numero-1)
        print(numero)
      
crescente(5)