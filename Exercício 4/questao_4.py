def crescente(num):
    if num == 0:
        print(0)
    else:
        crescente(num-1)
        return print(num)

crescente(5)